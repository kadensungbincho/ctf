var open = Module.findExportByName(null, "open");
Interceptor.attach(open, {
    onEnter(args) {
        console.log("Filename: " + args[0].readCString() + ", " + this.context.rdi.readCString());	// Android
        // console.log("Filename: " + args[0].readCString() + ", " + this.context.x0.readCString());	// iOS
        console.log("flags: " + args[1].toInt32() + ", " + this.context.rsi);	// Android
        // console.log("flags: " + args[1].toInt32() + ", " + this.context.x1);	// iOS
    },
    onLeave(retval) {
        console.log("ret: " + retval);
    }
});
