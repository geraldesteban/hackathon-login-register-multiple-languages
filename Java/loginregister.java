import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Account {
    public String firstName;
    public String lastName;
    public int age;
    public String username;
    public String password;
    public String email;

    public Account(String firstName, String lastName, int age, String username, String password, String email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
        this.username = username;
        this.password = password;
        this.email = email;
    }
}

public class loginregister {
    private static List<Account> accounts = new ArrayList<>();

    public static void main(String[] args) {
        // Initialize the accounts list with given data
        accounts.add(new Account("Ley", "Jivs", 22, "ley", "ley12345", "john@gmail.com"));
        accounts.add(new Account("Zero", "Johnson", 34, "zero", "zero12345", "zero@gmail.com"));
        accounts.add(new Account("Luxus", "Smith", 27, "luxus", "luxus12345", "luxus@gmail.com"));

        askLoginOrRegister();
    }

    public static void displayAccountsData() {
        System.out.println("----- Data Accounts Details ------");
        accounts.sort((a, b) -> a.firstName.compareTo(b.firstName));
        for (int i = 0; i < accounts.size(); i++) {
            Account acc = accounts.get(i);
            System.out.println((i + 1) + ": First name: " + acc.firstName + " lastname: " + acc.lastName
                    + " age: " + acc.age + " username: " + acc.username + " password: " + acc.password
                    + " email: " + acc.email);
        }
    }

    public static void askUserRegistration() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter name: ");
        String askName = scanner.nextLine();
        System.out.print("Enter last name: ");
        String askLastName = scanner.nextLine();
        System.out.print("Enter age: ");
        int askAge = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character
        System.out.print("Enter username: ");
        String askUserName = scanner.nextLine();

        String askPassword;
        while (true) {
            System.out.print("Enter password: ");
            askPassword = scanner.nextLine();
            if (askPassword.matches(".*\\d.*")) {
                break;
            } else {
                System.out.println("Invalid password! should have a number");
            }
        }

        String askEmail;
        while (true) {
            System.out.print("Enter email: ");
            askEmail = scanner.nextLine();
            if (askEmail.contains("@")) {
                accounts.add(new Account(askName, askLastName, askAge, askUserName, askPassword, askEmail));
                System.out.println("Registration successful!");
                askLoginOrRegister();
                return;
            } else {
                System.out.println("Invalid email! should have @");
            }
        }
    }

    public static void askUserLogin() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter username: ");
        String askUserName = scanner.nextLine();
        System.out.print("Enter password: ");
        String askPassword = scanner.nextLine();

        Account foundAccount = null;
        for (Account account : accounts) {
            if (account.username.equals(askUserName) && account.password.equals(askPassword)) {
                foundAccount = account;
                break;
            }
        }

        if (foundAccount != null) {
            displayAccountsData();
        } else {
            System.out.println("Invalid account!");
            askLoginOrRegister();
        }
    }

    public static void askLoginOrRegister() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Login or Register? ");
        String askUser = scanner.nextLine();

        if (askUser.equals("login")) {
            askUserLogin();
        } else if (askUser.equals("register")) {
            askUserRegistration();
        } else {
            System.out.println("Invalid input! should be Login or Register.");
            askLoginOrRegister();
        }
    }
}
