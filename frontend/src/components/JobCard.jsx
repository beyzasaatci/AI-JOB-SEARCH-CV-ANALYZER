import { useState } from "react";
import api from "../services/api";
import RecommendationCard from "./RecommendationCard";


function JobCard({ job }) {


  const [showRecommendation, setShowRecommendation] = useState(false);
  const [recommendation, setRecommendation] = useState(null);
  const [loading, setLoading] = useState(false);



  const score = Math.round(job.match_score);



  const getScoreStyle = () => {

    if(score >= 80){

      return {
        color:"text-green-700",
        bg:"bg-green-100",
        label:"🟢 Excellent Match"
      };

    }


    if(score >= 50){

      return {
        color:"text-yellow-700",
        bg:"bg-yellow-100",
        label:"🟡 Good Match"
      };

    }


    return {

      color:"text-red-700",
      bg:"bg-red-100",
      label:"🔴 Weak Match"

    };

  };



  const scoreStyle = getScoreStyle();





  const getRecommendation = async () => {


    if(showRecommendation){

      setShowRecommendation(false);
      return;

    }



    try{


      setLoading(true);



      const res = await api.post(

        `/jobs/${job.id}/recommendations`,

        {
          file_id:window.fileId
        }

      );



      setRecommendation(res.data);

      setShowRecommendation(true);



    }
    catch(err){

      console.log(err);

      alert(
        "AI Recommendation alınamadı"
      );

    }
    finally{

      setLoading(false);

    }


  };





return (

<div className="
bg-white
rounded-3xl
shadow-md
p-6
mb-6
border
hover:shadow-2xl
transition
">





<div className="
flex
justify-between
gap-5
">



<div>


<h2 className="
text-xl
font-bold
text-gray-800
">

{job.title}

</h2>




<p className="
text-blue-600
font-semibold
mt-2
">

🏢 {job.company}

</p>



<p className="
text-gray-500
mt-1
">

📍 {job.location}

</p>





{
job.work_type && (

<span className="
inline-block
mt-3
bg-blue-100
text-blue-700
px-3
py-1
rounded-full
text-sm
font-semibold
">

💻 {job.work_type}

</span>

)

}




{
job.salary && (

<span className="
inline-block
ml-2
bg-green-100
text-green-700
px-3
py-1
rounded-full
text-sm
font-semibold
">

💰 {job.salary}

</span>

)

}



</div>








<div className={`
${scoreStyle.bg}
${scoreStyle.color}
rounded-2xl
px-5
py-4
text-center
min-w-[120px]
`}>



<p className="
text-xs
font-semibold
">

AI MATCH

</p>



<p className="
text-3xl
font-bold
">

{score}%

</p>



<p className="
text-xs
mt-1
">

{scoreStyle.label}

</p>



</div>



</div>








<div className="
grid
grid-cols-2
gap-4
mt-6
">



<div className="
bg-gray-50
rounded-xl
p-4
">

🧠 Semantic

<strong className="
block
text-lg
">

{job.semantic_score}

</strong>


</div>






<div className="
bg-gray-50
rounded-xl
p-4
">

🛠 Skills

<strong className="
block
text-lg
">

{job.skill_score}

</strong>


</div>



</div>








<a

href={job.url}

target="_blank"

rel="noreferrer"

className="
block
mt-6
text-blue-600
font-bold
hover:underline
"

>

View Job →

</a>







<button

onClick={getRecommendation}

className="
mt-5
w-full
bg-gradient-to-r
from-purple-500
to-indigo-600
text-white
py-3
rounded-xl
font-bold
hover:scale-[1.02]
transition
"

>


{

loading

?

"🤖 AI Reviewing..."

:

showRecommendation

?

"Hide AI Recommendation"

:

"🤖 Show AI Recommendation"

}


</button>







{

showRecommendation && recommendation && (

<RecommendationCard

recommendation={recommendation}

/>

)

}



</div>

);


}


export default JobCard;