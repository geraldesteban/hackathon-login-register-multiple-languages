import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class LoginRegister {
    public static List<Account> accounts = new ArrayList<>();

    public static class Account {
        String firstName;
        String lastName;
        int age;
        String username;
        String password;
        String email;

        Account(String firstName, String lastName, int age, String username, String password, String email) {
            this.firstName = firstName;
            this.lastName = lastName;
            this.age = age;
            this.username = username;
            this.password = password;
            this.email = email;
        }
    }

    public static void main(String[] args) {
        // Add the provided accounts to the initial list
        accounts.add(new Account("Ley", "Jivs", 22, "ley", "ley12345", "ley@gmail.com"));
        accounts.add(new Account("Zero", "Johnson", 34, "zero", "zero12345", "zero@gmail.com"));
        accounts.add(new Account("Luxus", "Smith", 27, "luxus", "luxus12345", "luxus@gmail.com"));

        askLoginOrRegister();
    }

    public static void displaySortedAccounts() {
        System.out.println("----- Data Accounts Details ------");

        accounts.sort((acc1, acc2) -> acc1.firstName.toLowerCase().compareTo(acc2.firstName.toLowerCase()));

        for (int i = 0; i < accounts.size(); i++) {
            Account acc = accounts.get(i);
            System.out.println(i + 1 + ": First name: " + acc.firstName + " Last name: " + acc.lastName +
                    " Age: " + acc.age + " Username: " + acc.username + " Password: " + acc.password + " Email: " + acc.email);
        }
    }

    public static void askUserRegistration() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter name: ");
            String askName = scanner.nextLine();
            System.out.print("Enter last name: ");
            String askLastName = scanner.nextLine();
            System.out.print("Enter age: ");
            int askAge = scanner.nextInt();
            scanner.nextLine();  // Consume newline
            System.out.print("Enter username: ");
            String askUsername = scanner.nextLine();

            String askPassword = "";
            while (true) {
                System.out.print("Enter password: ");
                askPassword = scanner.nextLine();
                if (askPassword.matches(".*\\d.*")) {
                    break;
                } else {
                    System.out.println("Invalid password! Should have a number.");
                }
            }

            String askEmail = "";
            while (true) {
                System.out.print("Enter email: ");
                askEmail = scanner.nextLine();
                if (askEmail.contains("@")) {
                    Account newAccount = new Account(askName, askLastName, askAge, askUsername, askPassword, askEmail);
                    accounts.add(newAccount);
                    System.out.println("Registration successful!");
                    askLoginOrRegister();  // Call the login or register function again
                    break;
                } else {
                    System.out.println("Invalid email! Should have '@'.");
                }
            }
        }
    }

    public static void askUserLogin() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter username: ");
            String askUsername = scanner.nextLine();
            System.out.print("Enter password: ");
            String askPassword = scanner.nextLine();

            Account foundAccount = null;

            for (Account account : accounts) {
                if (account.username.equals(askUsername) && account.password.equals(askPassword)) {
                    foundAccount = account;
                    break;
                }
            }

            if (foundAccount != null) {
                System.out.println("Login successful!");
                displaySortedAccounts();  // Display sorted accounts after login
                System.exit(0);  // End the program
            } else {
                System.out.println("Invalid account!");
                askLoginOrRegister();  // Prompt user to log in or register again
            }
        }
    }

    public static void askLoginOrRegister() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Login or Register? ");

            String askUser = scanner.nextLine();

            if (askUser.equalsIgnoreCase("login")) {
                askUserLogin();
            } else if (askUser.equalsIgnoreCase("register")) {
                askUserRegistration();
            } else {
                System.out.println("Invalid input! Should be 'Login' or 'Register'.");
                askLoginOrRegister();
            }
        }
    }
}
