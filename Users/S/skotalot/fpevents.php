<?php


require 'scraperwiki/simple_html_dom.php';
                 $dom = new simple_html_dom();

foreach(range('A','Z') as $i) {
    $i = ucwords($i);

        $link = 'http://www.fpa.asn.au/default.asp?action=article&ID=21786-'.$i.'.htm';
        $html = scraperwiki::scrape($link);
        
        $images = array('jpg', 'jpeg');
        $maxX = 250;
        $maxY = 250;
        
        $dom->load($html);
        
        foreach ($dom->find('a') as $img) {
        
           scraperwiki::save(
            array('table_cell','table'), 
            array(
                'table_cell' => $img->plaintext,
                'table' => $img->getAttribute('href')
                )
            );
        
         }
    $i++;
    }
?><?php


require 'scraperwiki/simple_html_dom.php';
                 $dom = new simple_html_dom();

foreach(range('A','Z') as $i) {
    $i = ucwords($i);

        $link = 'http://www.fpa.asn.au/default.asp?action=article&ID=21786-'.$i.'.htm';
        $html = scraperwiki::scrape($link);
        
        $images = array('jpg', 'jpeg');
        $maxX = 250;
        $maxY = 250;
        
        $dom->load($html);
        
        foreach ($dom->find('a') as $img) {
        
           scraperwiki::save(
            array('table_cell','table'), 
            array(
                'table_cell' => $img->plaintext,
                'table' => $img->getAttribute('href')
                )
            );
        
         }
    $i++;
    }
?>