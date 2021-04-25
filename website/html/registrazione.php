<?php include("../server/server.php");?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrazione</title>


    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <!-- Link per il css del login -->
    <link rel="stylesheet" href="../css/layout.css">
    <link rel="stylesheet" href="../css/registrazione.css">
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
                <a class="p-2 text-muted" href="../webapp/game.html">GAME</a>
                <a class="p-2 text-muted" href="#">DOWNLOAD</a>
                <a class="p-2 text-muted" href="supporto.html">SUPPORTO TECNICO</a>
                <a class="p-2 text-muted" href="faq.html">FAQ</a>
                <a class="p-2 text-muted" href="contatti.html">CONTATTI</a>
            </nav>
        </div>

        <div class="containerIntestazione">
            <div class="row">
                <div id="testo">
                    <p>Creare un Account</p>
                </div>
            </div>
            <div class="row">
                <div class="col-md-2">
                    <?php include("../server/errors.php");?>
                    <form action="registrazione.php" method="POST">
                        <div class="formatCarattare">Nickname: <input type="text" name="nickname"></div>
                        <div class="formatCarattare">Email: <input type="text" name="email"></div>
                        <div class="formatCarattare">Nazionalità: <select name="naz">
                            <option value="AR">Argentina</option>
                            <option value="AU">Australia</option>
                            <option value="BR">Brazil</option>
                            <option value="CA">Canada</option>
                            <option value="CN">China</option>
                            <option value="FR">France</option>
                            <option value="DE">Germany</option>
                            <option value="IN">India</option>
                            <option value="ITA">Italy</option>
                            <option value="ENG">England</option>
                            <option value="JP">Japan</option>
                            <option value="NL">Netherlands</option>
                            <option value="US">United States</option>
                        </select></div>
                        <div class="formatCarattare">Anno⠀di⠀Nascita: <input type="date" name="dataN"></div>
                        <div class="formatCarattare">Password: <input type="text" name="password_1"></div>
                        <div class="formatCarattare">Conferma⠀Password: <input type="text" name="password_2"></div>
                        <br>
                        <input type="submit" name="reg_user" value="Conferma">
                    </form>
                </div>


                <div class="col-md-10">
                    <img src="../img/ape_logo.png" class="img" alt="Responsive image">
                </div>

            </div>
        </div>


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