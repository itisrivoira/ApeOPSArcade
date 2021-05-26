<?php include("../server/server.php");?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>


    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <!-- Link per il css del login -->
    <link rel="stylesheet" href="../css/layout.css">
    <link rel="stylesheet" href="../css/login.css">
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
                    <!--<div class="login">
                        <a href="./login.html">
                            <i class="fa fa-user-circle"></i> Login
                        </a>
                    </div>-->
                </div>
            </div>
        </header>

        <div class="nav-scroller py-1 mb-2">
            <nav class="nav d-flex justify-content-between">
                <a class="p-2 text-muted" href="../index.php">HOME</a>
                <a class="p-2 text-muted" href="../webapp/game.php">GAME</a>
                <a class="p-2 text-muted" href="download.php">DOWNLOAD</a>
                <a class="p-2 text-muted" href="supporto.php">SUPPORTO TECNICO</a>
                <a class="p-2 text-muted" href="faq.html">FAQ</a>
                <a class="p-2 text-muted" href="contatti.html">CONTATTI</a>
            </nav>
        </div>

        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-12" style="margin-left: 1rem;margin-right: 1rem;">
                    <img src="../img/ape_logo.png" class="img-fluid mx-auto d-block">

                    <div class="containerIntestazione">
                        <div class="row">
                            <div id="testo">
                                <p>Accedi</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-12">
                                <?php include("../server/errors.php");?>
                                <form action="login.php" method="POST">
                                    <input type="text" name="nickname" placeholder="nickname"><br>
                                    <input type="password" name="password" placeholder="password">
                                    <br>
                                    <input type="submit" name="login_user" value="login">
                                </form>
                            </div>
                        </div>
                        <br>
                        <div class="row">
                            <div class="col-md-12">
                                <p>Sei nuovo su APE OPS Arcade?</p>
                                <br>
                                <!-- creazione bottone link per file registrazione-->
                                <input type="submit" value="Registrati" onclick="document.location.href='registrazione.php'">
                            </div>
                        </div>
                        <br>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <footer class="bottom-footer">
        <div class="row">

            <div class="col-md-3">
                <h2 class="nomiSviluppatori">Sviluppatori: </h2>
                Riccardo Cherchi<br>
                <p>Lorenzo Miretti<br>Simone Francolino<br>Kevin Kadiasi<br>Stefano Pagliuzzi</p>
            </div>

            <div class="col-md-6">
                <h2 class="nomiSviluppatori">Il progetto: </h2>
                <p>Il progetto è nato a seguito della richiesta di una storia che fosse diversa dalle altre,una storia che doveva colpire dritto il cuore del giocatore.La storia doveva poi essere rappresentata sotto forma di gioco interattivo adatto a tutte
                    le età e che avesse come premessa una natura semplice e divertente.</p>
            </div>

            <div class="col-md-3">
                <h4 class="font-italic nomiSviluppatori">Informazioni Aggiuntive</h4>
                <ol class="list-unstyled">
                    <li>Visita la pagina di <a href="faq.html">faq</a></li>
                    <li>e la pagina <a href="contatti.html">contatti</a></li>
                </ol>

                <h4 class="font-italic nomiSviluppatori">Altrove</h4>
                <ol class="list-unstyled">
                    <li><a href="https://github.com/itisrivoira/ApeOPSArcade" target="_blank">GitHub</a></li>
                    <li><a href="http://dvgdib2zuodi32qidzh4yb3lu2ohp4z245ns5gmlzroamzcwa4za.b32.i2p/">I2P</a></li>
                </ol>
            </div>
        </div>
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
