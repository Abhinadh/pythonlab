<html>
<head>
<script>
function verify()
{
	if(document.forms.f1.n1.value=="")
	{
		window.alert("please fill the name");
		document.forms.f1.n1.focus();
	}
	else if(document.forms.f1.n2.value=="")
	{
		window.alert("please fill the address");
		document.forms.f1.n2.focus();
	}
	else if(document.forms.f1.n3.value=="")
	{
		window.alert("please fill the phone number");
		document.forms.f1.n3.focus();
	}
	else if(document.forms.f1.n4.value=="")
	{
		window.alert("please fill the gender");
		document.forms.f1.n4.focus();
	}
	else if(document.forms.f1.n5.value=="")
	{
		window.alert("please fill the dob");
		document.forms.f1.n5.focus();
	}
	else if(document.forms.f1.n6.value=="")
	{
		window.alert("please fill the relation");
		document.forms.f1.n6.focus();
	}
	else if(document.forms.f1.n8.value=="")
	{
		window.alert("please select the course");
		document.forms.f1.n8.focus();
	}
	else if(document.forms.f1.n9.value=="")
	{
		window.alert("please select the gender");
		document.forms.f1.n9.focus();
	}
}
</script>
<title>REGISTRATION FORM</title>
</head>
<body>

<h2 align="center" style="color:black">MAR ATHANASIUS COLLEGE OF
ENGINEERING</h2>
<h4 align="center" style="color:black">KOTHAMANGALAM, KERALA - 686
666</h4>
<h5 align="center" style="color:black">Ph : 0485 2522363,
www.mace.ac.in</h5><br><br>
<h3 align="center" style="color:black">REGISTRATION FORM</h3>

<form align="center" id="f1" onsubmit=" return verify()">

<table align="center" height="20%" width="23%" cellpadding="10" cellspacing="5">
<tr>
<td>NAME :</td>
<td><input type="text" placeholder="enter your name" id="n1"></td>
</tr>
<tr>
<td>GENDER :</td>
<td><input type="radio" name="gender" value="MALE" id="n4">
<label for="MALE">MALE</label><br>
<input type="radio" name="gender" value="FEMALE" id="n4">
<label for="FEMALE">FEMALE</label><br>
<input type="radio" name="gender" value="others" id="n4">
<label for="others">others</label><br></td>

</tr>
<tr>
<td>Date of Birth :</td>
<td><input type="date" placeholder="enter your dob" id="n5"></td>
</tr>
<tr>
<td>ADDRESS :</td>
<td><textarea placeholder="enter your address" id="n2"></textarea></td>
</tr>
<tr>
<td>PHONE :</td>
<td><input type="tel" placeholder="enter your phone number" id="n3"></td>
</tr>
<tr>
<td>Gaurdain Name :</td>
<td><input type="text" placeholder="enter the name" id="n9"></td>
</tr>
<tr>
<td>Relation with Guardian :</td>
<td><input type="radio" name="relation" value="Father" id="n6">
<label for="Father">Father</label><br>
<input type="radio" name="relation" value="Mother" id="n6">
<label for="Mother">Mother</label><br>
<input type="radio" name="relation" value="Others" id="n6">
<lable for="Others">Others</lable><br>
<input type="text" name="relation" placeholder="specify if any other"><br>
</td>
</tr>
<tr>
<td>Hobbies :</td>
<td><input type="checkbox" name="hobbies" value="Football" id="n7">
<label for="Football">Football</label><br>
<input type="checkbox" name="hobbies" value="Cricket" id="n7">
<label for="Cricket">Cricket</label><br>
<input type="checkbox" name="hobbies" value="Volleyball" id="n7">
<lable for="Volleyball">Volleyball</lable><br>
<input type="checkbox" name="hobbies" value="Basketball" id="n7" >
<lable for="Basketball">Basketball</lable><br>
<input type="checkbox" name="hobbies" value="Singing" id="n7">
<lable for="Singing">Singing</lable><br>
<input type="checkbox" name="hobbies" value="Dancing" id="n7">
<lable for="Dancing">Dancing</lable><br>
</td>
</tr>
<tr>
<td>Course :</td>
<td><select name="course" id="n8">
<option value="BCA">BCA</option>
<option value="BSC">BSC</option>
<option value="BA">BA</option>
</select>
</td>
</tr>
</table><br>
<input type="button" value="Submit" onclick="verify()">
</form>
</body>
</html> 
