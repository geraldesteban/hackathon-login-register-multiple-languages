"use strict";

// Data Storage of Accounts
const accounts = [
  {
    firstName: "Ley",
    lastName: "Jivs",
    age: 22,
    username: "ley",
    password: "ley12345",
    email: "john@gmail.com",
  },
  {
    firstName: "Zero",
    lastName: "Johnson",
    age: 34,
    username: "zero",
    password: "zero12345",
    email: "zero@gmail.com",
  },

  {
    firstName: "Luxus",
    lastName: "Smith",
    age: 27,
    username: "luxus",
    password: "luxus12345",
    email: "luxus@gmail.com",
  },
];

// Display Accounts Data
const displayAccountsData = () => {
  console.log("----- Data Accounts Details ------");
  accounts
    .slice()
    .sort((a, b) => a.firstName.localeCompare(b.firstName))
    .map((acc, i) => {
      console.log(
        `${i + 1}: First name: ${acc.firstName} lastname: ${
          acc.lastName
        } age: ${acc.age} username: ${acc.username} password: ${
          acc.password
        } email: ${acc.email}`
      );
    });
};

// Function for Reusable Asking User for Registration
const askUserRegistration = () => {
  const askName = prompt("Enter name: ");
  const askLastName = prompt("Enter last name: ");
  const askAge = Number(prompt("Enter age:"));
  const askUserName = prompt("Enter username: ");

  let askPassword;
  while (true) {
    askPassword = prompt("Enter password: ");
    if (/\d/.test(askPassword)) {
      break;
    } else {
      alert("Invalid password! should have number");
    }
  }

  let askEmail;
  // Keep asking for a valid email address
  while (true) {
    askEmail = prompt("Enter email: ");
    if (askEmail.includes("@")) {
      accounts.push({
        firstName: askName,
        lastName: askLastName,
        age: askAge,
        username: askUserName,
        password: askPassword,
        email: askEmail,
      });
      alert("Registration successful!");
      askLoginOrRegister(); // Prompt user to log in or register again
      return; // Exit the function after registration
    } else {
      alert("Invalid email! should have @");
    }
  }
};

// Function for Reusable Asking User for Login
const askUserLogin = () => {
  const askUserName = prompt("Enter username: ");
  const askPassword = prompt("Enter password: ");

  const foundAccount = accounts.find(
    account =>
      account.username === askUserName && account.password === askPassword
  );

  if (foundAccount) {
    displayAccountsData();
  } else {
    alert("Invalid account!");
    askLoginOrRegister(); // Prompt user to log in or register again
  }
};

// Function for Reusable Asking User for Login or Register
const askLoginOrRegister = () => {
  const askUser = prompt("Login or Register?");

  if (askUser === "login") {
    askUserLogin();
  } else if (askUser === "register") {
    askUserRegistration();
  } else {
    alert("Invalid input! should be Login or Register.");
    askLoginOrRegister();
  }
};

// First Step Ask User to Login or Register
askLoginOrRegister();
