// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAZVHdbRVAfh1ZMy9r8cmxxJFIPw5ppFYE",
  authDomain: "projetocroqui-8cc78.firebaseapp.com",
  databaseURL: "https://projetocroqui-8cc78-default-rtdb.firebaseio.com",
  projectId: "projetocroqui-8cc78",
  storageBucket: "projetocroqui-8cc78.firebasestorage.app",
  messagingSenderId: "437874947245",
  appId: "1:437874947245:web:f8cfcc141b290be1338224"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);
