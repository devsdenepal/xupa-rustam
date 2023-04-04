<?php

$user_name="";

$psd="";

if(isset($_GET['user_name'])){

    $user_name = $_GET['user_name'];

    $psd = $_GET['user_pass'];

    if($user_name == 'gautam' && $psd=='123456789'){

      echo '<h1>LOGGINED</h1>';

    }

    else{

        echo '<h1>Login attemped failed...<h1>';

    }

    

}

?>
