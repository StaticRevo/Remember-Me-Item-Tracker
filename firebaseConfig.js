// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAUdDfRQVjzHbfoOGJql3YXL-kAwidu1Jg",
  authDomain: "remembermeapp-84b23.firebaseapp.com",
  projectId: "remembermeapp-84b23",
  storageBucket: "remembermeapp-84b23.firebasestorage.app",
  messagingSenderId: "42314919219",
  appId: "1:42314919219:web:ca6b735e46883514ad2246",
  measurementId: "G-DLN05360N2"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);