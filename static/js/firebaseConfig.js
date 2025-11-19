// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBSTukLnlg7pOzGC3WRrGpReT6gx3xnDIA",
  authDomain: "frontenders-c9373.firebaseapp.com",
  projectId: "frontenders-c9373",
  storageBucket: "frontenders-c9373.firebasestorage.app",
  messagingSenderId: "762635999906",
  appId: "1:762635999906:web:f7086af71ae351d67915fb",
  measurementId: "G-BZQZGXB9NB"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

