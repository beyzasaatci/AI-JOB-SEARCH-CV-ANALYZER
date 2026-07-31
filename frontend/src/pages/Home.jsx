import { useState, useEffect } from "react";
import UploadBox from "../components/UploadBox";
import JobCard from "../components/JobCard";
import { BriefcaseBusiness } from "lucide-react";
import { motion } from "framer-motion";

function Home() {
  const [analysisResult, setAnalysisResult] = useState(null);

  useEffect(() => {
    const handleAnalysisUpdate = (e) => {
      setAnalysisResult(e.detail);
    };

    window.addEventListener("cvAnalyzed", handleAnalysisUpdate);
    return () => {
      window.removeEventListener("cvAnalyzed", handleAnalysisUpdate);
    };
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 selection:bg-cyan-400/30 selection:text-cyan-200 font-sans antialiased relative overflow-hidden">

      {/* Belirgin, Geniş Alan Kaplayan ve Soldan Sağa Akıp Giden Canlı Renk Dalgaları */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden z-0">
        <motion.div
          animate={{
            x: ["-35%", "35%", "-35%"],
            y: ["-10%", "15%", "-10%"],
            scale: [1, 1.2, 1],
          }}
          transition={{
            duration: 7,
            repeat: Infinity,
            ease: "easeInOut",
          }}
          className="absolute top-[-20%] left-[-20%] w-[900px] h-[900px] bg-cyan-400/35 rounded-full blur-[140px]"
        />
        <motion.div
          animate={{
            x: ["35%", "-35%", "35%"],
            y: ["15%", "-15%", "15%"],
            scale: [1.1, 0.9, 1.1],
          }}
          transition={{
            duration: 9,
            repeat: Infinity,
            ease: "easeInOut",
          }}
          className="absolute top-[10%] right-[-20%] w-[900px] h-[900px] bg-blue-500/35 rounded-full blur-[140px]"
        />
        <motion.div
          animate={{
            x: ["-20%", "25%", "-20%"],
            y: ["10%", "-10%", "10%"],
            scale: [0.9, 1.2, 0.9],
          }}
          transition={{
            duration: 8,
            repeat: Infinity,
            ease: "easeInOut",
          }}
          className="absolute bottom-[-20%] left-[15%] w-[1000px] h-[1000px] bg-teal-400/30 rounded-full blur-[160px]"
        />
      </div>

      {/* Subtle Grid Texture */}
      <div className="absolute inset-0 bg-[linear-gradient(to_right,#ffffff08_1px,transparent_1px),linear-gradient(to_bottom,#ffffff08_1px,transparent_1px)] bg-[size:3.5rem_3.5rem] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)] pointer-events-none z-0" />

      {/* Navbar */}
      <nav className="w-full border-b border-white/[0.1] backdrop-blur-2xl bg-slate-900/40 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto flex justify-between items-center px-8 py-4">

          <div className="flex items-center gap-3">
            <div className="bg-gradient-to-br from-cyan-400/30 to-blue-500/30 border border-cyan-400/40 p-2.5 rounded-xl shadow-lg backdrop-blur-md">
              <BriefcaseBusiness
                size={22}
                className="text-cyan-300"
              />
            </div>
            <div>
              <h1 className="font-bold text-base text-white tracking-tight">
                AI Career Matcher <span className="text-[10px] px-2 py-0.5 rounded-full bg-cyan-400/20 text-cyan-300 border border-cyan-400/30 font-mono ml-1.5">PRO</span>
              </h1>
              <p className="text-xs text-slate-300 font-mono">
                Neural Job Discovery Engine
              </p>
            </div>
          </div>

        </div>
      </nav>

      {/* Hero Section / Main Layout */}
      <section className="max-w-7xl mx-auto px-8 py-16 relative z-10">

        <div className="grid lg:grid-cols-12 gap-12 items-start">

          {/* LEFT SIDE: Analiz Sonuçları / Karşılama Ekranı */}
          <div className="lg:col-span-7 space-y-8">
            
            {analysisResult && analysisResult.matches ? (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                className="space-y-6"
              >
                <div className="flex items-center justify-between bg-slate-900/60 border border-white/[0.1] p-6 rounded-2xl backdrop-blur-2xl shadow-[0_16px_32px_-12px_rgba(0,0,0,0.3)]">
                  <div>
                    <h2 className="text-xl font-bold text-white tracking-tight flex items-center gap-2">
                      <span>🎯</span> Matched Career Opportunities
                    </h2>
                    <p className="text-xs font-mono text-slate-300 mt-1">
                      File: <span className="text-cyan-300">{analysisResult.filename}</span> • {analysisResult.job_count} jobs found
                    </p>
                  </div>
                  <button
                    onClick={() => setAnalysisResult(null)}
                    className="text-xs font-mono text-slate-200 hover:text-white bg-slate-800/60 border border-white/[0.1] px-3.5 py-2 rounded-xl transition hover:bg-slate-700/80 cursor-pointer backdrop-blur-md"
                  >
                    🔄 Upload New CV
                  </button>
                </div>

                <div className="space-y-6">
                  {analysisResult.matches.map((job) => (
                    <JobCard
                      key={`${analysisResult.file_id}-${job.id}`}
                      job={job}
                    />
                  ))}
                </div>
              </motion.div>
            ) : (
              <motion.div
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
                className="space-y-8"
              >
                <div>
                  <span className="
                  bg-cyan-400/15
                  border
                  border-cyan-400/30
                  text-cyan-200
                  px-4
                  py-1.5
                  rounded-full
                  font-mono
                  text-xs
                  tracking-wide
                  backdrop-blur-md
                  inline-block
                  mb-4
                  shadow-inner
                  ">
                    ⚡ Autonomous Resume Telemetry
                  </span>

                  <h1 className="
                  text-4xl
                  lg:text-5xl
                  font-extrabold
                  leading-[1.1]
                  text-white
                  tracking-tight
                  ">
                    Find Your
                    <span className="bg-gradient-to-r from-cyan-300 via-blue-200 to-teal-200 bg-clip-text text-transparent">
                      {" "}Dream Job
                    </span>
                    <br />
                    At Light Speed.
                  </h1>

                  <p className="
                  text-slate-200
                  text-base
                  mt-4
                  leading-relaxed
                  font-normal
                  ">
                    Upload your resume on the right panel for deep semantic parsing. Our neural orchestrator aligns your background across global databases to surface top-tier career placements right here.
                  </p>
                </div>

                {/* Awaiting State Box */}
                <div className="rounded-3xl bg-slate-900/40 border border-white/[0.1] p-10 text-center backdrop-blur-2xl border-dashed shadow-[0_16px_32px_-12px_rgba(0,0,0,0.3)]">
                  <div className="text-4xl mb-3 animate-pulse">📡</div>
                  <h3 className="text-sm font-mono font-semibold text-slate-100">Awaiting Resume Telemetry</h3>
                  <p className="text-xs font-mono text-slate-300 mt-1 max-w-sm mx-auto">
                    Your matched career listings will stream dynamically in this left column immediately upon upload.
                  </p>
                </div>

                {/* Stats Grid */}
                <div className="grid grid-cols-3 gap-6 pt-6 border-t border-white/[0.1]">
                  <div className="bg-slate-900/50 border border-white/[0.08] p-5 rounded-2xl backdrop-blur-xl">
                    <h2 className="text-2xl font-extrabold text-white font-mono">50K+</h2>
                    <p className="text-xs text-slate-300 font-mono mt-1">Active Listings</p>
                  </div>
                  <div className="bg-slate-900/50 border border-white/[0.08] p-5 rounded-2xl backdrop-blur-xl">
                    <h2 className="text-2xl font-extrabold text-white font-mono">96.8%</h2>
                    <p className="text-xs text-slate-300 font-mono mt-1">Semantic Precision</p>
                  </div>
                  <div className="bg-slate-900/50 border border-white/[0.08] p-5 rounded-2xl backdrop-blur-xl">
                    <h2 className="text-2xl font-extrabold text-white font-mono">28+</h2>
                    <p className="text-xs text-slate-300 font-mono mt-1">Global Hubs</p>
                  </div>
                </div>
              </motion.div>
            )}

          </div>

          {/* RIGHT SIDE: Upload Box */}
          <div className="lg:col-span-5 lg:sticky lg:top-28">
            <motion.div
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.6, delay: 0.1 }}
            >
              <UploadBox />
            </motion.div>
          </div>

        </div>

      </section>

    </div>
  );
}

export default Home;