<?php
    session_start();

    if (isset($_GET['logout'])) {
		session_destroy();
		unset($_SESSION);
		header("location: ../index.php");
	}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOWNLOAD</title>


    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <!-- Link per il css del download -->
    <link rel="stylesheet" href="../css/layout.css">
    <!-- devo mettere il css di download-->
    <link rel="stylesheet" href="../css/download.css">
</head>

<?php if (isset($_SESSION['nickname'])): ?>
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
                    <?php if (isset($_SESSION['nickname'])): ?>
                        <p>Benvenuto <strong><?php echo $_SESSION['nickname']; ?></strong></p>
			            <p> <a href="download.php?logout='1'" style="color: red;"> logout</a> </p>
		            <?php endif ?>
                </div>
            </div>
        </header>

        <div class="nav-scroller py-1 mb-2">
            <nav class="nav d-flex justify-content-between">
                <a class="p-2 text-muted" href="../index.php">HOME</a>
                <a class="p-2 text-muted" href="../webapp/game.html">GAME</a>
                <a class="p-2 text-muted" href="downloa.html">DOWNLOAD</a>
                <a class="p-2 text-muted" href="supporto.html">SUPPORTO TECNICO</a>
                <a class="p-2 text-muted" href="faq.html">FAQ</a>
                <a class="p-2 text-muted" href="contatti.html">CONTATTI</a>
            </nav>
        </div>


        <div class="container">
            <!-- Immagini contorno-->
            <img src="../img/brigadiereRuspa.png" class="immagineSinistra">
            <img src="../img/protag.png" class="immagineDestra">


            <div class="containerDownload">
                <div class="row">
                    <div class="col-md-12">
                        <div class="titolo">DOWNLOAD</div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12">
                        <div>
                            <br>
                            <p  class="testo">Per scaricare APE OPS Arcade...<br>Clicca sul pulsante di download<br> e preparati ad una fantastica avventura</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-12">
                    <!-- Bottone download -->
                    <a href="../server/risorse/risorse.php" download="risorse">
                        <img src="../img/downloadBottone.jpeg" class="imgDownload" alt="risorse.php">
                    </a>
                </div>
            </div>
        </div>

        <footer class="bottom-footer">
            <p>Creato e modificato da <a href="https://github.com/lollomire">Miretti Lorenzo</a></p>
            <p>
                <a href="../index.html">Torna all'inizio</a>
            </p>
        </footer>


        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script>
            window.jQuery || document.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"><\/script>')
        </script>


        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js "></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js "></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/holder/2.9.7/holder.min.js "></script>


</body>
<?php else:?>
    <body class="bg-dark text-white py-5">
        <div class="container py-5">
            <div class="row">
                <div class="col-md-3 text-center">
                    <p id="immagineAlert"><i class="fa fa-exclamation-triangle fa-5x" id="immagineAlert"></i><br/>Status Code: 403</p>
                </div>
                <div class="col-md-9">
                    <h3>OPPSSS!!!! Sorry...</h3>
                    <p>Per poter accedere alla pagina hai bisogno di eseguire prima il login<br/>Perfavore esegui il login e riprova</p>
                    <a class="btn btn-danger" href="javascript:history.back()">Torna indietro</a>
                </div>
            </div>
        </div>
    </body>
<?php endif ?>

</html>