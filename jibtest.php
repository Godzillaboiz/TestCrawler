<?php

$file = file('tmp/Crawl.json');
foreach($file as $k)
    $json[] = explode(',',$k);

    print_r($json);

?>