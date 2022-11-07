Open CV Detection App<br>

<?php

$dir = "./data/haarcascades/";
$dir = scandir($dir);

echo '<form action="./opencv-php-upload-process.php" method="post" enctype="multipart/form-data">';
echo '<select name="filter">';
foreach($dir as $folder){
        echo '<option value="'.$folder.'">'.$folder.'</option>';
}

echo "</select>";
echo "<br><br>";
echo '<label for="files">Select files:</label>';
echo '<input type="file" id="files" name="files[]" multiple><br><br>';

echo '<input type="submit" value="Process Pictures">';
echo '</form>';

echo '<a href="opencv-upload-php-delete-pics.php?delete=yes"> Delete Uploaded Pictures</a><br><br>';

?>