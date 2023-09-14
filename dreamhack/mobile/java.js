Java.perform(function() {
    var context = Java.use('android.app.ActivityThread').currentApplication().getApplicationContext();
    var toast = Java.use("android.widget.Toast");
    toast.makeText(context, Java.use("java.lang.String").$new("Welcome to Dreamhack"), 1).show();
});
