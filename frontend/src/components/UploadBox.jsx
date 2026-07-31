import { useState, useEffect } from "react";
import api from "../services/api";
import JobCard from "./JobCard";


function UploadBox() {

  const [file, setFile] = useState(null);

  const [country, setCountry] = useState("Turkey");

  const [city, setCity] = useState("");

  const [locations, setLocations] = useState({});

  const [loading, setLoading] = useState(false);

  const [step, setStep] = useState(0);

  const [result, setResult] = useState(null);



  const steps = [
    "📄 Uploading CV",
    "🧠 Extracting Skills",
    "🔎 Searching Jobs",
    "🎯 Matching Opportunities",
    "🤖 AI Review"
  ];



  useEffect(() => {

    api.get("/locations")
      .then((res)=>{
        setLocations(res.data);
      })
      .catch((err)=>{
        console.log(
          "Locations error:",
          err
        );
      });

  }, []);





  const upload = async()=>{


    if(!file){

      alert("Please select CV");

      return;

    }


    if(!city){

      alert("Please select city");

      return;

    }



    try{


      setLoading(true);



      let current = 0;


      const interval = setInterval(()=>{

        current++;

        if(current < steps.length){

          setStep(current);

        }

      },1200);





      const formData = new FormData();


      formData.append(
        "file",
        file
      );


      formData.append(
        "location",
        `${country} ${city}`
      );




      const res = await api.post(
        "/upload-cv",
        formData
      );



      clearInterval(interval);



      setStep(steps.length-1);



      setResult(
        res.data
      );


      window.fileId =
        res.data.file_id;




    }
    catch(err){


      console.log(
        err
      );


      alert(
        err.response?.data?.detail ||
        "Upload failed"
      );


    }
    finally{

      setTimeout(()=>{

        setLoading(false);

      },800);

    }

  };






return (

<div className="
min-h-screen
w-full
bg-gradient-to-br
from-slate-900
via-blue-900
to-slate-800
flex
items-center
justify-center
p-6
">


<div className="
bg-white/95
backdrop-blur
max-w-5xl
w-full
rounded-3xl
shadow-2xl
p-10
border
border-blue-100
">





<div className="text-center">


<div className="
text-6xl
animate-bounce
">

🚀

</div>



<h1 className="
text-5xl
font-extrabold
text-blue-900
mt-4
tracking-tight
">

AI Job Matcher

</h1>



<p className="
text-slate-500
text-lg
mt-3
">

AI analyzes your CV and finds the best career opportunities.

</p>



</div>







{
loading && (

<div className="
mt-8
bg-blue-50
rounded-2xl
p-6
">


<h2 className="
text-xl
font-bold
text-blue-700
mb-5
">

🤖 AI is working...

</h2>




{
steps.map((item,index)=>(


<div

key={item}

className={`
flex
items-center
gap-3
mb-3
text-lg
${
index <= step
?
"text-green-600 font-semibold"
:
"text-gray-400"
}
`}

>


<span>

{
index < step
?
"✅"
:
index === step
?
"⏳"
:
"○"
}

</span>


{item}


</div>


))

}


</div>

)

}








<div className="
mt-10
">


<label

htmlFor="cv-upload"

className="
cursor-pointer
block
border-2
border-dashed
border-blue-300
rounded-3xl
p-12
text-center
bg-blue-50/50
hover:bg-blue-100
hover:border-blue-600
transition-all
duration-300
"


>



<div className="
text-6xl
">

📄

</div>



<h2 className="
text-xl
font-bold
mt-4
">

Upload your CV

</h2>


<p className="
text-gray-400
mt-2
">

Click anywhere or drag your file here

</p>


<p className="
text-sm
text-gray-400
">

PDF / DOCX up to 5MB

</p>




<input

id="cv-upload"

type="file"

hidden

accept=".pdf,.docx"

onChange={(e)=>
setFile(e.target.files[0])
}

/>


</label>




{
file && (

<div className="
mt-4
bg-green-50
border
border-green-200
rounded-xl
p-4
text-green-700
font-semibold
">

✅ {file.name}

</div>

)

}



</div>









<div className="
grid
grid-cols-2
gap-5
mt-8
">



<select

value={country}

onChange={(e)=>{

setCountry(e.target.value);

setCity("");

}}

className="
border
rounded-xl
p-4
"

>


{
Object.keys(locations).map((c)=>(

<option

key={c}

value={c}

>

🌍 {c}

</option>

))

}


</select>






<select

value={city}

onChange={(e)=>setCity(e.target.value)}

className="
border
rounded-xl
p-4
"

>


<option>

🏙 Select City

</option>



{
locations[country]?.map((c)=>(

<option

key={c}

value={c}

>

{c}

</option>

))

}



</select>



</div>










<button

onClick={upload}

disabled={loading}

className="
mt-8
w-full
bg-blue-700
hover:bg-blue-800
text-white
py-5
rounded-2xl
text-xl
font-bold
shadow-md
hover:shadow-xl
transition-all
duration-300
disabled:opacity-50
"

>

{
loading
?
"🤖 AI Analyzing..."
:
"🚀 Analyze My CV"
}


</button>









{
result && (

<div className="
mt-10
border-t
pt-8
">


<h2 className="
text-3xl
font-bold
mb-5
">

🎯 Matched Jobs

</h2>



<div className="
bg-gray-50
rounded-xl
p-5
mb-6
">


<p>
<strong>CV:</strong> {result.filename}
</p>


<p>
<strong>Jobs Found:</strong> {result.job_count}
</p>


</div>





{
result.matches?.map((job)=>(


<JobCard

key={`${result.file_id}-${job.id}`}

job={job}

/>


))

}




</div>

)

}



</div>


</div>

);


}


export default UploadBox;