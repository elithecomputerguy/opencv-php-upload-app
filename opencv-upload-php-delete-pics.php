<?php

if (isset($_GET['delete'])){
    shell_exec("rm upload/*");
}

$opencv_result = shell_exec("python3 opencv-php-upload-python.py");

if($opencv_result !=""){
    header("Location: ./picture.php");
} else {
    echo "problem";
}

?>