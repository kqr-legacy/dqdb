<?php

mb_internal_encoding("UTF-8");
include('database.php');
mysql_query("set names utf8;");

$query = "SELECT * FROM qdb_quotes";
$result = mysql_query($query);

while ($row = mysql_fetch_array($result)) {
        $pubdate = $row['pubdate'];
        $hash = $row['hash'];
        $quote = str_replace('\r\n', "\n", $row['quote']);
	$quote = str_replace("\r", '', $quote);
	$quote = str_replace("\\'", "'", $quote);
	$quote = str_replace('\\"', '"', $quote);
        echo("$pubdate\n$hash\n$quote\n");
        echo("~\n");
}
?>
 
