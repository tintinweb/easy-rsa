#!/usr/syno/synoman/webman/3rdparty/EASYRSA/php-cli
<?php
DEFINE("PWD",realpath(dirname(__FILE__)));						//path to this script#
DEFINE("EASY_RSA",PWD."/openvpn_easy-rsa/easy-rsa/2.0");		//path to easy-rsa scripts


################## START #######################
print "Content-Type: text/html\n\n";

#### 1) Check permissions
if (!has_permissions()){
    die("You are not allowed to access this page!");
}

#### 2) perform user action
# get user query
parse_str($_SERVER['QUERY_STRING'], $QUERY);

switch($QUERY['action']){
    case 'reset':
    		easy_rsa_exec("./clean-all > log.txt");
    		print file_get_contents(EASY_RSA."/log.txt");
    		print "OK!";
    		break;
    	
    case 'buildca':
    		easy_rsa_exec("./shell-build-ca");
    		print "OK!";
    		break;
    case 'builddh':
        	easy_rsa_exec("./shell-build-dh");
        	print "OK!";
    		break;
    case 'buildkeyserver':
      		easy_rsa_exec("./shell-build-key-server server");
      		print "OK!";
    		break;
    case 'buildkeyclient':
        	easy_rsa_exec("./shell-build-key client1");
        	print "OK!";
    		break;
    default:
            #print "default";

}

function easy_rsa_exec($cmd){

	return pwd_exec(EASY_RSA,"source ./vars && $cmd");
}

function pwd_exec($pwd, $cmd){
	$pwd=escapeshellarg($pwd);
	
	print "cd $pwd && $cmd";
	return exec("cd $pwd && $cmd");
}

function has_permissions(){
        $user= exec("/usr/syno/synoman/webman/modules/authenticate.cgi");
        return $user==="admin";
}

?>
<html>
<head>
    <title>EasyRSA</title>
    <link rel="stylesheet" type="text/css" href="/scripts/ext-3/resources/css/ext-all.css"/>
	<!-- yup, I'm mixing themes from both versions, gives a bit more native look -->
    <link rel="stylesheet" type="text/css" href="/scripts/ext-3/resources/css/xtheme-gray.css"/>
    <script type="text/javascript" src="/scripts/ext-3/adapter/ext/ext-base.js"></script>
    <script type="text/javascript" src="/scripts/ext-3/ext-all.js"></script>
</head>
<body>

<script type="text/javascript">



function estimateHeight() {
	var myWidth = 0, myHeight = 0;
	if( typeof( window.innerWidth ) == 'number' ) {
		//Non-IE
		myHeight = window.innerHeight;
	} else if( document.documentElement && ( document.documentElement.clientWidth || document.documentElement.clientHeight ) ) {
		//IE 6+ in 'standards compliant mode'
		myHeight = document.documentElement.clientHeight;
	} else if( document.body && ( document.body.clientWidth || document.body.clientHeight ) ) {
		//IE 4 compatible
		myHeight = document.body.clientHeight;
	}
	return myHeight;
}


Ext.onReady(function() {

	var conn = new Ext.data.Connection();

	
    function onResetBtnClick(item){
		conn.request({
			url: 'index.cgi?'+Ext.urlEncode({action:'reset'}),
			success: function(responseObject) {
				Ext.Msg.alert('Status',responseObject.responseText);
			}
		});
	}
	
    function onBuildCABtnClick(item){
		conn.request({
			url: 'index.cgi?'+Ext.urlEncode({action:'buildca'}),
			success: function(responseObject) {
				Ext.Msg.alert('Status',responseObject.responseText);
			}
		});
	}

    function onBuildDhBtnClick(item){
		conn.request({
			url: 'index.cgi?'+Ext.urlEncode({action:'builddh'}),
			success: function(responseObject) {
				Ext.Msg.alert('Status',responseObject.responseText);
			}
		});
	}

    function onBuildKeyServerBtnClick(item){
		conn.request({
			url: 'index.cgi?'+Ext.urlEncode({action:'buildkeyserver'}),
			success: function(responseObject) {
				Ext.Msg.alert('Status',responseObject.responseText);
			}
		});
	}	


    function onBuildKeyClientBtnClick(item){
		conn.request({
			url: 'index.cgi?'+Ext.urlEncode({action:'buildkeyclient'}),
			success: function(responseObject) {
				Ext.Msg.alert('Status',responseObject.responseText);
			}
		});
	}

	var resetBtn = new Ext.Toolbar.Button({
		handler: onResetBtnClick,
		name: 'reset',
		text: 'Reset',
		icon: 'images/cert32.png',
		cls: 'x-btn-text-icon',
		disabled: false
	});
	
	var buildCaBtn = new Ext.Toolbar.Button({
		handler: onBuildCABtnClick,
		name: 'buildca',
		text: 'BuildCA',
		icon: 'images/cert32.png',
		cls: 'x-btn-text-icon',
		disabled: false
	});
	
	var buildDhBtn = new Ext.Toolbar.Button({
		handler: onBuildDhBtnClick,
		name: 'builddh',
		text: 'BuildDH',
		icon: 'images/cert32.png',
		cls: 'x-btn-text-icon',
		disabled: false
	});
	
	var buildKeyServerBtn = new Ext.Toolbar.Button({
		handler: onBuildKeyServerBtnClick,
		name: 'buildkeyserver',
		text: 'BuildKeyServer',
		icon: 'images/cert32.png',
		cls: 'x-btn-text-icon',
		disabled: false
	});

	var buildKeyClientBtn = new Ext.Toolbar.Button({
		handler: onBuildKeyClientBtnClick,
		name: 'buildkeyclient',
		text: 'BuildKeyClient',
		icon: 'images/cert32.png',
		cls: 'x-btn-text-icon',
		disabled: false
	});

	
    var form = new Ext.FormPanel({
    	renderTo: 'content',
        baseCls: 'x-plain',
        url:'save-form.php',
		height: estimateHeight(),
        items: [
			new Ext.Toolbar({
				items: [
					'-',
					resetBtn,
					'-',
					buildCaBtn,
					'-',
					buildDhBtn,
					'-',
					buildKeyServerBtn,
					'-',
					buildKeyClientBtn,
					'-',
				]
			}),
		]
    });


	Ext.EventManager.onWindowResize(function() {
		form.doLayout();
		form.setHeight(estimateHeight());
	});


});




</script>
<DIV id="content"></DIV>

</body>
</html>