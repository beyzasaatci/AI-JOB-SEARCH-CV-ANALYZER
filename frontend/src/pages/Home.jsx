import UploadBox from "../components/UploadBox";


function Home(){

return (

<div className="
min-h-screen
bg-gradient-to-br
from-slate-100
via-blue-50
to-slate-200
flex
flex-col
items-center
justify-center
p-6
">


<div className="
text-center
mb-8
">


<h1 className="
text-5xl
font-extrabold
text-slate-800
">

AI Career Matcher

</h1>


<p className="
mt-3
text-lg
text-slate-600
">

AI-powered CV analysis and job matching platform

</p>


</div>



<UploadBox />


</div>

);

}


export default Home;