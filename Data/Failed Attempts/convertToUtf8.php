<?php
$text=file_get_contents("wikt.words");
//$text="\u{092e}\u0941\u0916\u092a\u0943\u0937\u094d\u0920";

$text = preg_replace_callback('/\\\\u([0-9a-fA-F]{4})/', function ($match) {
    return mb_convert_encoding(pack('H*', $match[1]), 'UTF-8', 'UCS-2BE');
}, $text);

file_put_contents("hindi.words",pack("CCC",0xef,0xbb,0xbf).$text);
