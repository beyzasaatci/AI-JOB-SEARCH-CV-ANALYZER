function RecommendationCard({ recommendation }) {


  const score = recommendation.overall_fit_score || 0;



  return (

    <div className="
      mt-6
      bg-gradient-to-br
      from-purple-50
      to-white
      border
      border-purple-200
      rounded-3xl
      p-6
      shadow-sm
    ">



      <h3 className="
        text-2xl
        font-extrabold
        text-purple-700
        mb-6
      ">

        🤖 AI Career Analysis

      </h3>







      {/* SCORE */}


      <div className="
        bg-white
        rounded-2xl
        p-5
        mb-6
        shadow
      ">


        <div className="
          flex
          justify-between
          mb-3
        ">


          <span className="font-semibold">

            Overall Fit

          </span>


          <span className="
            text-purple-600
            font-bold
            text-xl
          ">

            {score}/100

          </span>


        </div>





        <div className="
          w-full
          bg-gray-200
          rounded-full
          h-4
        ">


          <div

          className="
          h-4
          bg-gradient-to-r
          from-purple-500
          to-pink-500
          rounded-full
          "

          style={{
            width:`${score}%`
          }}

          />



        </div>



      </div>









{/* STRENGTHS */}

{
recommendation.strengths && (

<div className="
mb-6
">


<h4 className="
font-bold
text-green-700
mb-3
">

💪 Your Strengths

</h4>



<div className="
flex
flex-wrap
gap-2
">


{
recommendation.strengths.map((item)=>(

<span

key={item}

className="
bg-green-100
text-green-700
px-3
py-2
rounded-full
text-sm
font-semibold
"

>

✅ {item}

</span>


))

}


</div>


</div>


)

}









{/* SKILL GAP */}


{
recommendation.skill_gap && (

<div className="
mb-6
">


<h4 className="
font-bold
text-orange-600
mb-3
">

📊 Skill Gap Analysis

</h4>




{

Object.entries(
recommendation.skill_gap
).map(([skill,value])=>(


<div

key={skill}

className="
mb-3
">


<div className="
flex
justify-between
text-sm
mb-1
">

<span>

{skill}

</span>


<span>

{value}%

</span>


</div>





<div className="
bg-gray-200
rounded-full
h-3
">


<div

className="
bg-orange-400
h-3
rounded-full
"

style={{
width:`${value}%`
}}

/>



</div>



</div>



))


}




</div>


)

}










{/* MISSING SKILLS */}



<div className="
mb-6
">


<h4 className="
font-bold
text-red-600
mb-3
">

❌ Missing Skills

</h4>



<div className="
bg-white
rounded-xl
p-4
">


<ul className="
list-disc
ml-5
">


{

recommendation.missing_skills?.map((skill)=>(


<li key={skill}>

{skill}

</li>


))


}


</ul>


</div>


</div>













{/* IMPROVEMENT */}



<div className="
mb-6
">


<h4 className="
font-bold
text-blue-600
mb-3
">

🚀 Improvement Plan

</h4>



<div className="
bg-white
rounded-xl
p-4
">


<ul className="
list-disc
ml-5
">


{

recommendation.improvement_suggestions?.map((item)=>(


<li key={item}>

{item}

</li>


))


}


</ul>


</div>


</div>












{/* REDUNDANT */}


<div className="
mb-6
">


<h4 className="
font-bold
text-gray-700
mb-3
">

🗑 Remove / Improve

</h4>



<ul className="
list-disc
ml-5
">


{

recommendation.redundant_content?.map((item)=>(

<li key={item}>

{item}

</li>

))


}


</ul>


</div>













{/* JUSTIFICATION */}



<div className="
bg-white
rounded-xl
p-5
">


<h4 className="
font-bold
mb-2
">

💡 AI Explanation

</h4>


<p className="
text-gray-600
leading-relaxed
">

{recommendation.justification}

</p>



</div>







</div>


  );

}


export default RecommendationCard;