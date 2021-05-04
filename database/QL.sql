INSERT INTO utente VALUES($nickname,$password,$email,$naz,$dataNascita);

SELECT utente.Nickname FROM utente
WHERE utente.Nickname = $nickname AND utente.Password = $password;

SELECT * FROM utente 
WHERE utente.Nickname = $nickname;

SELECT * FROM utente 
WHERE utente.Email = $email;

SELECT * FROM utente
WHERE utente.Nickname = $nickname AND utente.Password = $password;

UPDATE utente SET utente.Nickname = $nickname WHERE utente.Nickname = $oldNickname;
UPDATE utente SET utente.Email = $email WHERE utente.Nickname = $nickname;
UPDATE utente SET utente.Password = $password WHERE utente.Nickname = $nickname;
UPDATE utente SET utente.Nazione = $naz WHERE utente.Nickname = $nickname;
