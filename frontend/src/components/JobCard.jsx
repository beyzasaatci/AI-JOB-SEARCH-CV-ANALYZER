import { useState } from "react";
import api from "../services/api";
import RecommendationCard from "./RecommendationCard";

function JobCard({ job }) {
  const [showRecommendation, setShowRecommendation] = useState(false);
  const [recommendation, setRecommendation] = useState(null);
  const [loading, setLoading] = useState(false);

  const score = Math.round(job.match_score || 0);
  const skillScore = Math.round(job.skill_score || 0);

  const getScoreStyle = () => {
    if (skillScore >= 70) {
      return {
        text: "text-cyan-300",
        border: "border-cyan-400/20",
        bg: "bg-cyan-400/10",
        label: "Optimal Skills Match"
      };
    }
    if (skillScore >= 20) {
      return {
        text: "text-blue-300",
        border: "border-blue-400/20",
        bg: "bg-blue-400/10",
        label: "Moderate Alignment"
      };
    }
    return {
      text: "text-teal-300",
      border: "border-teal-400/20",
      bg: "bg-teal-400/10",
      label: "Baseline Alignment"
    };
  };

  const scoreStyle = getScoreStyle();

  const getRecommendation = async () => {
    if (showRecommendation) {
      setShowRecommendation(false);
      return;
    }

    try {
      setLoading(true);
      const res = await api.post(
        `/jobs/${job.id}/recommendations`,
        {
          file_id: window.fileId
        }
      );
      setRecommendation(res.data);
      setShowRecommendation(true);
    } catch (err) {
      console.log(err);
      alert("AI Recommendation alınamadı");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="rounded-3xl bg-slate-900/60 border border-white/[0.1] backdrop-blur-2xl p-6 sm:p-8 shadow-[0_16px_32px_-12px_rgba(0,0,0,0.4)] hover:border-cyan-400/40 transition-all duration-300 relative overflow-hidden group">
      
      {/* Background Architectural Mesh (Mavi/Camgöbeği Tonları) */}
      <div className="absolute top-0 right-0 w-[250px] h-[250px] bg-gradient-to-bl from-cyan-500/10 via-blue-500/5 to-transparent blur-[80px] pointer-events-none" />

      <div className="relative z-10">
        <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-5">
          
          <div className="space-y-1.5">
            <h2 className="text-xl font-bold text-white tracking-tight">
              {job.title}
            </h2>

            <p className="text-cyan-300 font-mono text-xs flex items-center gap-1.5">
              <span>🏢</span> {job.company}
            </p>

            <p className="text-slate-300 text-xs font-mono flex items-center gap-1.5">
              <span>📍</span> {job.location}
            </p>

            <div className="flex flex-wrap gap-2 pt-2">
              {job.work_type && (
                <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md bg-slate-950/60 border border-white/[0.08] text-xs font-mono text-slate-300">
                  💻 {job.work_type}
                </span>
              )}

              {job.salary && (
                <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md bg-cyan-500/10 border border-cyan-500/20 text-xs font-mono text-cyan-200">
                  💰 {job.salary}
                </span>
              )}
            </div>
          </div>

          {/* AI Match Badge Card */}
          <div className={`${scoreStyle.bg} ${scoreStyle.border} border rounded-2xl px-5 py-4 text-center min-w-[130px] backdrop-blur-md shadow-lg shrink-0`}>
            <p className="text-[10px] font-mono tracking-wider text-slate-300 uppercase">
              AI MATCH
            </p>
            <p className={`text-3xl font-extrabold font-mono mt-0.5 ${scoreStyle.text}`}>
              {score}%
            </p>
            <p className="text-[11px] font-mono mt-1 text-slate-200">
              {scoreStyle.label}
            </p>
          </div>

        </div>

        {/* Metrics Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-6 font-mono">
          <div className="bg-slate-950/60 border border-white/[0.08] rounded-xl p-4">
            <span className="text-xs text-slate-400 uppercase tracking-wider block mb-1">🧠 Semantic Match</span>
            <strong className="text-lg text-slate-200 font-mono">
              {job.semantic_score}
            </strong>
          </div>

          <div className="bg-slate-950/60 border border-white/[0.08] rounded-xl p-4">
            <span className="text-xs text-slate-400 uppercase tracking-wider block mb-1">🛠 Skills Alignment</span>
            <strong className="text-lg text-slate-200 font-mono">
              {job.skill_score}
            </strong>
          </div>
        </div>

        {/* Action Bar */}
        <div className="mt-6 flex flex-col sm:flex-row items-center justify-between gap-4">
          <a
            href={job.url}
            target="_blank"
            rel="noreferrer"
            className="text-xs font-mono text-cyan-300 hover:text-cyan-200 transition-colors flex items-center gap-1 group/link"
          >
            <span>View Job Spec</span>
            <span className="group-hover/link:translate-x-0.5 transition-transform">→</span>
          </a>
        </div>

        {/* AI Recommendation Trigger Button */}
        <button
          onClick={getRecommendation}
          disabled={loading}
          className="mt-6 w-full bg-gradient-to-r from-cyan-400 via-blue-500 to-teal-400 hover:from-cyan-300 hover:to-blue-400 text-slate-950 py-3.5 px-4 rounded-2xl text-xs font-mono font-bold tracking-wider shadow-[0_0_25px_rgba(34,211,238,0.2)] hover:shadow-[0_0_35px_rgba(34,211,238,0.35)] border border-white/40 transition-all duration-300 cursor-pointer flex items-center justify-center space-x-2 disabled:opacity-50"
        >
          {loading ? (
            <>
              <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-slate-950" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
              </svg>
              <span>AI REVIEWING PAYLOAD...</span>
            </>
          ) : showRecommendation ? (
            <span>HIDE AI RECOMMENDATION</span>
          ) : (
            <span>🤖 GENERATE AI RECOMMENDATION</span>
          )}
        </button>

        {/* Recommendation Result Card - Expanded full width to remove dead space */}
        {showRecommendation && recommendation && (
          <div className="mt-6 pt-6 border-t border-white/[0.08]">
            <RecommendationCard recommendation={recommendation} />
          </div>
        )}

      </div>
    </div>
  );
}

export default JobCard;