import { useState, useEffect } from "react";
import api from "../services/api";

function UploadBox() {
  const [file, setFile] = useState(null);
  const [country, setCountry] = useState("");
  const [city, setCity] = useState("");
  const [locations, setLocations] = useState({});
  const [loading, setLoading] = useState(false);
  const [step, setStep] = useState(0);

  const steps = [
    "📄 Uploading CV",
    "🧠 Extracting Skills",
    "🔎 Searching Jobs",
    "🎯 Matching Opportunities",
    "🤖 AI Review"
  ];

  useEffect(() => {
    api.get("/locations")
      .then((res) => {
        setLocations(res.data);
        // ponytail: varsayilani hardcode etmiyoruz, ulke listesi degisince kirilmasin
        setCountry(Object.keys(res.data)[0] ?? "");
      })
      .catch((err) => console.error("LOCATIONS FAILED:", api.defaults.baseURL, err));
  }, []);

  const upload = async () => {
    if (!file) {
      alert("Please select CV");
      return;
    }

    if (!city) {
      alert("Please select city");
      return;
    }

    try {
      setLoading(true);
      let current = 0;
      const interval = setInterval(() => {
        current++;
        if (current < steps.length) {
          setStep(current);
        }
      }, 1200);

      const formData = new FormData();
      formData.append("file", file);
      formData.append("location", `${country} ${city}`);

      const res = await api.post("/upload-cv", formData);

      clearInterval(interval);
      setStep(steps.length - 1);
      window.fileId = res.data.file_id;

      window.dispatchEvent(
        new CustomEvent("cvAnalyzed", { detail: res.data })
      );

    } catch (err) {
      console.log(err);
      alert(err.response?.data?.detail || "Upload failed");
    } finally {
      setTimeout(() => {
        setLoading(false);
      }, 800);
    }
  };

  return (
    <div className="rounded-3xl bg-slate-900/40 border-2 border-cyan-400/40 backdrop-blur-2xl p-8 sm:p-10 shadow-[0_0_50px_rgba(34,211,238,0.25)] relative overflow-hidden">
      
      {/* Daha Parlak ve Yoğun Arka Plan Mesh Efekti */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-[350px] bg-gradient-to-b from-cyan-400/25 via-blue-500/15 to-transparent blur-[90px] pointer-events-none" />

      <div className="relative z-10">

        {/* Header Section */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-gradient-to-br from-cyan-400/30 to-blue-500/30 border border-cyan-400/50 text-3xl mb-4 shadow-[0_0_20px_rgba(34,211,238,0.4)] animate-pulse">
            🚀
          </div>
          
          <h2 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight drop-shadow-md">
            AI Job Matcher
          </h2>
          
          <p className="text-cyan-200 text-sm mt-2 max-w-sm mx-auto font-mono">
            Neural telemetry analyzes your CV for career alignment.
          </p>
        </div>

        {/* Loading Progress State */}
        {loading && (
          <div className="mb-6 rounded-2xl bg-slate-950/90 border border-cyan-400/40 p-6 backdrop-blur-xl shadow-[0_0_20px_rgba(34,211,238,0.15)]">
            <h3 className="text-xs font-mono text-cyan-300 mb-3 flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-cyan-400 animate-ping" />
              🤖 AI Pipeline Execution Active...
            </h3>

            <div className="space-y-2.5 font-mono text-xs">
              {steps.map((item, index) => (
                <div
                  key={item}
                  className={`flex items-center gap-2.5 transition-colors ${
                    index <= step ? "text-cyan-200 font-medium" : "text-slate-500"
                  }`}
                >
                  <span>
                    {index < step ? "✅" : index === step ? "⏳" : "○"}
                  </span>
                  <span>{item}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Upload Box Dropzone */}
        <div>
          <label
            htmlFor="cv-upload"
            className="cursor-pointer block border-2 border-dashed border-cyan-400/30 rounded-3xl p-10 text-center bg-slate-950/50 hover:bg-slate-950/80 hover:border-cyan-400/70 transition-all duration-300 group shadow-[inset_0_0_20px_rgba(34,211,238,0.05)]"
          >
            <div className="text-5xl mb-4 group-hover:scale-110 transition-transform duration-300">
              📄
            </div>

            <h3 className="text-base font-semibold text-white font-mono">
              Upload your CV
            </h3>
            
            <p className="text-cyan-200 text-xs mt-1.5 font-mono">
              Click or drag & drop document
            </p>
            
            <p className="text-[11px] text-slate-400 font-mono mt-1">
              PDF / DOCX up to 5MB
            </p>

            <input
              id="cv-upload"
              type="file"
              hidden
              accept=".pdf,.docx"
              onChange={(e) => setFile(e.target.files[0])}
            />
          </label>

          {file && (
            <div className="mt-4 bg-cyan-500/20 border border-cyan-400/40 rounded-2xl p-4 text-cyan-100 font-mono text-xs flex items-center gap-3 backdrop-blur-md shadow-[0_0_15px_rgba(34,211,238,0.2)]">
              <span className="text-base">✅</span>
              <span className="truncate">{file.name}</span>
            </div>
          )}
        </div>

        {/* Location Selectors */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-5 mt-7">
          <div className="space-y-2">
            <label className="block text-xs font-mono font-semibold text-cyan-300 tracking-wider">
              COUNTRY
            </label>
            <select
              value={country}
              onChange={(e) => {
                setCountry(e.target.value);
                setCity("");
              }}
              className="w-full bg-slate-950/90 border border-cyan-400/40 hover:border-cyan-400 text-slate-100 rounded-2xl px-5 py-4 text-sm font-mono focus:outline-none focus:border-cyan-400 focus:ring-2 focus:ring-cyan-400/30 transition-all shadow-inner cursor-pointer"
            >
              {Object.keys(locations).map((c) => (
                <option key={c} value={c} className="bg-slate-900 text-slate-100 py-2">
                  🌍 {c}
                </option>
              ))}
            </select>
          </div>

          <div className="space-y-2">
            <label className="block text-xs font-mono font-semibold text-cyan-300 tracking-wider">
              CITY
            </label>
            <select
              value={city}
              onChange={(e) => setCity(e.target.value)}
              className="w-full bg-slate-950/90 border border-cyan-400/40 hover:border-cyan-400 text-slate-100 rounded-2xl px-5 py-4 text-sm font-mono focus:outline-none focus:border-cyan-400 focus:ring-2 focus:ring-cyan-400/30 transition-all shadow-inner cursor-pointer"
            >
              <option value="" className="bg-slate-900 text-slate-400 py-2">
                🏙 Select City
              </option>
              {locations[country]?.map((c) => (
                <option key={c} value={c} className="bg-slate-900 text-slate-100 py-2">
                  {c}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Submit Action Button */}
        <button
          onClick={upload}
          disabled={loading}
          className="mt-8 w-full bg-gradient-to-r from-cyan-400 via-blue-400 to-teal-300 hover:from-cyan-300 hover:to-blue-300 text-slate-950 py-4 px-6 rounded-2xl text-xs sm:text-sm font-mono font-bold tracking-wider shadow-[0_0_30px_rgba(34,211,238,0.4)] hover:shadow-[0_0_45px_rgba(34,211,238,0.6)] border border-white/60 transition-all duration-300 disabled:opacity-50 cursor-pointer flex items-center justify-center space-x-2"
        >
          {loading ? (
            <>
              <svg className="animate-spin -ml-1 mr-2 h-5 w-5 text-slate-950" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
              </svg>
              <span>AI ANALYZING...</span>
            </>
          ) : (
            <span>🚀 ANALYZE MY CV</span>
          )}
        </button>

      </div>
    </div>
  );
}

export default UploadBox;