// Most of the code is from: https://cloud.google.com/appengine/docs/standard/python3/building-app/authenticating-users

// Listener for lcick on sign-out button
window.addEventListener('load', function () {
  document.getElementById('sign-out').onclick = function () {
    console.log('Signed out');
    firebase.auth().signOut();
  };

  // FirebaseUI config.
  var uiConfig = {
    signInSuccessUrl: '/',
    signInOptions: [
      firebase.auth.GoogleAuthProvider.PROVIDER_ID
    ],
  };

  // Usere signed in or out behaviour.
  firebase.auth().onAuthStateChanged(function (user) {
    if (user) {
      // User is signed in, so display the "sign out" button and login info.
      document.getElementById('login-info').style.display = "flex";
      console.log(`Signed in as ${user.displayName} (${user.email})`);
      user.getIdToken().then(function (token) {
        document.cookie = "token=" + token;
      });
    } else {
      // User is signed out, FirebaseUI init and display login button
      var ui = new firebaseui.auth.AuthUI(firebase.auth());
      ui.start('#firebaseui-auth-container', uiConfig);
      document.getElementById('login-info').style.display = "none";
      // Clear the token cookie.
      document.cookie = "token=";
    }
  }, function (error) {
    console.log(error);
    alert('Unable to log in: ' + error)
  });
});
