/*
    fabric javascript<->python bridge core
    a bridging layer between python and javascript for GtkWebKit
*/

/**
 * issue a bridge call to fabric
 * @param {string} function_name
 * @param {array<string>} args
 * @param {number} id
 * @returns {any}
 */
function doInvokeWebkitBridgeCall(function_name, args, id) {
    if (!window.webkit) {
        throw new Error(
            "window.webkit is not defined, can't call " + function_name
        );
    }
    return window.webkit.messageHandlers.fabricJsBridge.postMessage(
        JSON.stringify([function_name, args, id])
    );
}

window.fabric = {
    _init_called: false,
    _pool: {},
    bridge: {},
    init: () => {
        if (window.fabric._init_called) {
            return;
        }
        window.fabric._init_called = true;
        window.dispatchEvent(new CustomEvent("bridgeReady"));
    },

    /**
     * create a bridge object for a foreign python function
     * @param {Map} func_list
     *     {func: string, args: Array}
     */
    createBridge: (func_list) => {
        for (var i = 0; i < func_list.length; i++) {
            var element = func_list[i];
            var func_name = element.func;
            var args = element.args;
            var func_hierarchy = func_name.split(".");
            var function_name = func_hierarchy.pop();
            var nested_object = func_hierarchy.reduce((obj, prop) => {
                if (!obj[prop]) {
                    obj[prop] = {};
                }
                return obj[prop];
            }, window.fabric.bridge);
            var func_body = `
                var __id__ = (Math.random() + "").substring(2);

                doInvokeWebkitBridgeCall("${func_name}", arguments, __id__);
                var promise = new Promise(
                    function(resolve, reject) {
                        window.fabric.checkReturnValue("${func_name}", resolve, reject, __id__);
                    }
                );

                return promise;
            `;
            nested_object[function_name] = new Function(args, func_body);
            window.fabric._pool[func_name] = {};
        }
    },

    /**
     * check the return value of a foreign function
     * @param {string} func_name
     * @param {function} resolve
     * @param {function} reject
     * @param {number} id
     */
    checkReturnValue: (func_name, resolve, reject, id) => {
        // this is not a good idea, but it works anyways
        // a better way to implement this is to use a state managed model
        // TODO: the above...
        var check = setInterval(function () {
            var return_obj = window.fabric._pool[func_name][id];
            if (return_obj) {
                var value = return_obj.value;
                var error = return_obj.error;

                delete window.fabric._pool[func_name][id];
                clearInterval(check);

                if (error) {
                    var python_error = JSON.parse(value);
                    var error = new Error(python_error.message);
                    error.name = python_error.name;
                    error.stack = python_error.stack;

                    reject(error);
                } else {
                    resolve(JSON.parse(value));
                }
            }
        }, 1);
    },
};

window.fabric.init();
