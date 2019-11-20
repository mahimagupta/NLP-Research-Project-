<?php

$han=fopen('hiwiki-20191020-pages-articles-multistream.xml','r');
$flagOpen=false;
file_put_contents("hindi.txt",pack("CCC",0xef,0xbb,0xbf)."\n");
while($data=fgets($han)){
	if(!$flagOpen && ($pos=strpos($data,'<text'))!==false){
		$pos=strpos($data,'>',$pos);
		$flagOpen=true;
		echo trim($data)."\n";
		$data=substr($data,$pos+1);
	}
	if($flagOpen && ($pos=strpos($data,'</text'))!==false){
		$flagOpen=false;
		$data=substr($data,0,$pos);
		//$data=preg_replace('/[a-zA-Z\[\]#{}`~@&\.!;"<>\/\\$%^*\(\)\-=\+,“”\'_%]/','',$data);
		$data=preg_replace('/[a-zA-Z\[\]#{}`~@&\.!;"<>\/\\$%^*\(\)\-=\+,\'_%]/','',$data);
		echo trim($data);
		if(!$data) continue;
		$data.="\n";
		$out=fopen('hindi.txt','a');
		fwrite($out,$data);
		fclose($out);

	}
}
fclose($han);