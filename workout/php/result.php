<?php 
session_start();

$con= mysqli_connect('localhost','root','','workout');

$usermovementid = $_SESSION['id'];
$useridmovementstr = implode ("",$_SESSION['usermovementid']);

$sql = "SELECT result.type,movementresult.ResultPercentage, movementresult.DumbbellWeight, movementresult.avgVelocity  FROM result,movementresult Where movementresult.usermovementid = $useridmovementstr AND movementresult.resultID = result.id ";
$result=mysqli_query($con,$sql);
$data = mysqli_fetch_assoc($result);
$datastr = implode (" ",$data);
$res = explode(" ", $datastr);

$sql2 = "SELECT repInfo FROM movementresult Where movementresult.usermovementid = $useridmovementstr ";
$result2 =mysqli_query($con,$sql2);
$data2 = mysqli_fetch_assoc($result2);
$datastr2 = implode (" ",$data2);
$reps = explode(" ", $datastr2);

$sql3 = "SELECT velocityInfo FROM movementresult Where movementresult.usermovementid = $useridmovementstr ";
$result3 =mysqli_query($con,$sql3);
$data3 = mysqli_fetch_assoc($result3);
$datastr3 = implode (" ",$data3);
$velocity = explode(" ", $datastr3);

$sql4 = "SELECT avgVelocity FROM movementresult Where movementresult.usermovementid = $useridmovementstr";
$result4 = mysqli_query($con,$sql4);
$data4 = mysqli_fetch_assoc($result4);
$datastr4 = implode (" ",$data4);
//echo "$data";
$x=1;
$y=0;

if(isset($_POST['submit']))
{
   header("location: HomePage.php" );
}

?>

<html>
<head>
<title>Result</title>
<link rel="stylesheet" href="../css/result.css">
</head>



<body>
 
<form method="post"  name="forma">
<image src="../images/gym7.png" width="100px" height="50px" align="left" id="a1">
<image src="../images/gym7.png" width="100px" height="50px" align="right" id="a2">
<h1> Your Workout Result </h1>
<br>
<h2><span style='color:hotpink'>Dumbbell Weight : </span><?php echo $res[3]?> Kg</h2>
<br>
<h2><?php foreach($reps as $value){
	
  echo "<p><span style='color:hotpink'>Rep $x :</span> $value";
  echo " | <span style='color:hotpink'>Velocity :</span> $velocity[$y] m/sec</p>";
  $x+=1;
  $y+=1;
} ?></h2>

<br>
<h2><span style='color:hotpink'>Overall Result : </span><?php echo $res[0]?></h2>

<h2><span style='color:hotpink'>Average Velocity : </span><?php echo $datastr4?>%</h2>
<br><br>
<input type="submit"  name="submit" value="Back To Home" id="button">
</form>

</body>
</html>