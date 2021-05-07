<?php



    
    USE PHPMailer\PHPMailer\PHPMailer;
    use PHPMailer\PHPMailer\Exception;
  

    
    if(isset($_POST['Invia'])){ 
        // $nick indica il nickname del mittente
        $nick = $_POST['Nickname'];
        // $email indica la mail del mittente
        $email = $_POST['email'];
        //  $testo indica il testo all'interno della mail del mittente
        $testo = $_POST['testo'];

        // $subject indica il titolo della mail
        $subject = 'Recapito supporto tecnico';

        require_once "PHP-MAIL/PHPMailer.php";
        require_once "PHP-MAIL/SMTP.php";
        require_once "PHP-MAIL/POP3.php";
        require_once "PHP-MAIL/Exception.php";

        // creo nuovo oggetto PHPMailer
        $mail = new PHPMailer();

        //Impostazioni SMTP
        $mail->IsSMTP();
        $mail->Host = "smtp.gmail.com"; //imposto come mail host quello di gmail stmp cioè posta uscente
        $mail->SMTPAuth = true; //serve per dire se esiste o no un autenticazione
        $mail->Username = "apeopsarcade@gmail.com";    // metto l'emai di APE SUPPORTO TECNICO
        $mail->Password = "APE20215C"; //password dell account APE
        $mail->Port = 465; //porta del server di posta in uscita(PORTA FISSA DI GMAIL)
        $mail->SMTPSecure = 'ssl';  //serve ad impostare la sicurezza con il protocollo tls

        // Impostazioni email
        $mail->IsHTML();
        $mail->setFrom($email, $nick);
        $mail->AddAddress("apeopsarcade@gmail.com");
        $mail->Subject = ("$email ($subject)"); 
        $mail->Body = $testo;

        if(!$mail->Send()){
            echo "errore nell'invio della mail: ".$mail->ErrorInfo;
            return false;
        }else{
            return true;
        }

    }

?>

    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>


        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

        <!-- Icons -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

        <!-- Link per il css del login -->
        <link rel="stylesheet" href="../css/layout.css">
        <link rel="stylesheet" href="../css/supporto.css">
    </head>

    <body>
        <div class="container">
            <header class="main-header py-3">
                <div class="row flex-nowrap justify-content-between align-items-center">
                    <div class="col-4 pt-1">
                        <p></p>
                        <!--Colonna per riempire spazio vuoto-->
                    </div>
                    <div class="col-4 text-center">
                        <a class="main-header-logo text-dark" href="#">APE OPS Arcade</a>
                    </div>
                    <div class="col-4 d-flex justify-content-end align-items-center">
                        <div class="login">
                            <a href="login.php">
                                <i class="fa fa-user-circle"></i> Login
                            </a>
                        </div>
                    </div>
                </div>
            </header>

            <div class="nav-scroller py-1 mb-2">
                <nav class="nav d-flex justify-content-between">
                    <a class="p-2 text-muted" href="../index.php">HOME</a>
                    <a class="p-2 text-muted" href="../webapp/game.html">GAME</a>
                    <a class="p-2 text-muted" href="#">DOWNLOAD</a>
                    <a class="p-2 text-muted" href="faq.html">FAQ</a>
                    <a class="p-2 text-muted" href="contatti.html">CONTATTI</a>
                </nav>
            </div>
        </div>

        <!-- Immagini contorno-->
        <img src="../img/dottoreCheRide.png" class="immagineSinistra">
        <img src="../img/chef.png" class="immagineDestra">

        <div class="contenitorePrincipale">
            <p id="titolo">Supporto APE OPS Arcade</p>
            <div id="intestazione">
                <br> Per inviare un email al supporto tecnico, </br>
                <br> compila il seguente modulo. </br>
            </div>
            <form action="supporto.php" method="post">
                <div class="supporto">
                    <br>Nickname:</br>
                    <input type="text" name="Nickname" id="Nickname">
                    <br>
                    <br>Email:</br>
                    <input type="text" name="email" id="email">
                    <br>
                    <br>Testo:</br>
                    <input type="text" name="testo" id="testo">
                    <br>
                    <br>
                    <input type="submit" name="Invia" value="Invia">
                    <br>
                </div>
            </form>
        </div>



        <footer class="bottom-footer">
            <p>Creato e modificato da <a href="https://github.com/lollomire">Miretti Lorenzo.</a></p>
        </footer>

        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script>
            window.jQuery || document.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"><\/script>')
        </script>


        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js "></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js "></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/holder/2.9.7/holder.min.js "></script>



    </body>

    </html>