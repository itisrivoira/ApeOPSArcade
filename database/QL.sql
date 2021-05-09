INSERT INTO utente VALUES($nickname,$password,$email,$naz,$dataNascita);
INSERT INTO tasti VALUES($codiceT,$descrizione);
INSERT INTO salvataggio VALUES ($codS,$data,$tempo,$punteggio,$nickname);

SELECT utente.Nickname FROM utente
WHERE utente.Nickname = $nickname AND utente.Password = $password;

SELECT * FROM utente 
WHERE utente.Nickname = $nickname;

SELECT * FROM utente 
WHERE utente.Email = $email;

SELECT * FROM utente
WHERE utente.Nickname = $nickname AND utente.Password = $password;

SELECT * FROM utente 
WHERE utente.DataN = $dataNascita;

SELECT * FROM tasti
WHERE tasti.nickname = $nickname;

SELECT * FROM tasti
WHERE tasti.descrizione = $descrizione;

SELECT * FROM salvataggio
WHERE salvataggio.codiceS = $codS;

SELECT * FROM salvataggio
WHERE salvataggio.data = $data;

SELECT * FROM salvataggio
WHERE salvataggio.tempo = $tempo;

SELECT * FROM salvataggio
WHERE salvataggio.punteggio = $punteggio;

SELECT * FROM salvataggio
WHERE salvataggio.nickname = $nickname;



UPDATE utente SET utente.Nickname = $nickname WHERE utente.Nickname = $oldNickname;
UPDATE utente SET utente.Email = $email WHERE utente.Nickname = $nickname;
UPDATE utente SET utente.Password = $password WHERE utente.Nickname = $nickname;
UPDATE utente SET utente.Nazione = $naz WHERE utente.Nickname = $nickname;
UPDATE utente SET utente.DataN = $dataNascita WHERE utente.Nickname = $nickname;
UPDATE configura SET configura.codiceTasto = $codiceT WHERE configura.codiceTasto = $codiceT;
UPDATE configura SET configura.descrizione = $descrizione WHERE configura.codiceTasto = $codiceT;



