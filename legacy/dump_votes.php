<?php

mb_internal_encoding("UTF-8");
include('database.php');
mysql_query("set names utf8;");

$query = "SELECT * FROM qdb_votes";
$result = mysql_query($query);

while ($row = mysql_fetch_array($result)) {
          $hash = $row['hash'];
                  $ip = $row['ip'];
                  echo("$hash,$ip\n");
}
?>
