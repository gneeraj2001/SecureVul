#include <iostream>
#include <mysql/jdbc.h>
int main() { // connect to MySQL database using JDBC driver, take SQL query from user, execute the query, and print the result
    std::cout << "Enter a SQL query: ";
    std::string query;
    std::cin >> query;
    std::cout << "Enter a username: ";
    std::string username;
    std::cin >> username;
    std::cout << "Enter a password: ";
    std::string password;
    std::cin >> password;
    std::cout << "Enter a database name: ";
    std::string database;
    std::cin >> database;
    std::cout << "Enter a host name: ";
    std::string host;
    std::cin >> host;
    std::cout << "Enter a port number: ";
    std::string port;
    std::cin >> port;
    std::cout << "Enter a driver name: ";
    std::string driver;
    std::cin >> driver;
    std::cout << "Enter a connection URL: ";
    std::string url;
    std::cin >> url;
    std::cout << "Enter a connection properties: ";
    std::