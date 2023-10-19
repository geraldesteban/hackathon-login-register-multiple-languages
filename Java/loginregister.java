import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

class Account {
    private String firstName;
    private String lastName;
    private int age;
    private String username;
    private String password;
    private String email;

    public Account(String firstName, String lastName, int age, String username, String password, String email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.username = username;
        this.password = password;
        this.email = email;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getPassword() {
        return password;
    }

    @Override
    public String toString() {
        return "First name: " + firstName + " Last name: " + lastName + " Age: " + age + " Username: " + username + " Password: " + password + " Email: " + email;
    }
}

public class loginregister {
    public static void main(String[] args) {
        List<Account> accounts = new ArrayList<>();

        // Provided account details
        Account account1 = new Account("Ley", "Jivs", 22, "ley", "ley12345", "john@gmail.com");
        Account account2 = new Account("Zero", "Johnson", 34, "zero", "zero12345", "zero@gmail.com");
        Account account3 = new Account("Luxus", "Smith", 27, "luxus", "luxus12345", "luxus@gmail.com");

        // Add the provided accounts to the list
        accounts.add(account1);
        accounts.add(account2);
        accounts.add(account3);

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Login or Register?");
            String choice = scanner.next();

            if (choice.equals("login")) {
                askUserLogin(accounts, scanner);
            } else if (choice.equals("register")) {
                askUserRegistration(accounts, scanner);
            } else {
                System.out.println("Invalid input! Should be 'Login' or 'Register'.");
            }
        }
    }

    private static void displaySortedAccounts(List<Account> accounts) {
        System.out.println("----- Data Accounts Details ------");

        // Sort accounts by firstName (case-insensitive)
        Collections.sort(accounts, (a1, a2) -> a1.getFirstName().compareToIgnoreCase(a2.getFirstName()));

        // Iterate through the sorted accounts and print the details
        for (int i = 0; i < accounts.size(); i++) {
            System.out.println((i + 1) + ": " + accounts.get(i));
        }
    }

    private static void askUserRegistration(List<Account> accounts, Scanner scanner) {
        while (true) {
            System.out.println("Enter name: ");
            String firstName = scanner.next();
            System.out.println("Enter last name: ");
            String lastName = scanner.next();
            System.out.println("Enter age: ");
            int age = scanner.nextInt();
            System.out.println("Enter username: ");
            String username = scanner.next();

            while (true) {
                System.out.println("Enter password: ");
                String password = scanner.next();
                if (password.matches(".*\\d+.*")) {
                    break;
                } else {
                    System.out.println("Invalid password! Should have a number");
                }
            }

            while (true) {
                System.out.println("Enter email: ");
                String email = scanner.next();
                if (email.contains("@")) {
                    Account newAccount = new Account(firstName, lastName, age, username, password, email);
                    accounts.add(newAccount);
                    System.out.println("Registration successful!");

                    // Display the updated and sorted list of accounts
                    displaySortedAccounts(accounts);

                    System.out.println("Do you want to log in or register another account? (Login/Register/Exit): ");
                    String choice = scanner.next().toLowerCase();
                    if (choice.equals("login")) {
                        askUserLogin(accounts, scanner);
                        break;
                    } else if (choice.equals("register")) {
                        continue;  // Register another account
                    } else if (choice.equals("exit")) {
                        break;
                    } else {
                        System.out.println("Invalid choice!");
                    }
                } else {
                    System.out.println("Invalid email! Should have '@'");
                }
            }
        }
    }

    private static void askUserLogin(List<Account> accounts, Scanner scanner) {
        System.out.println("Enter username: ");
        String username = scanner.next();
        System.out.println("Enter password: ");
        String password = scanner.next();

        Account foundAccount = null;

        for (Account account : accounts) {
            if (account.getFirstName().equals(username) && account.getPassword().equals(password)) {
                foundAccount = account;
                break;
            }
        }

        if (foundAccount != null) {
            displaySortedAccounts(accounts);
        } else {
            System.out.println("Invalid account!");
        }
    }
}
