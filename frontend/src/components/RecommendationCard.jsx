function RecommendationCard({ recommendation }) {
  const score = recommendation.overall_fit_score || 0;

  return (
    <div className="rounded-2xl bg-zinc-950/80 border border-white/[0.08] backdrop-blur-2xl p-6 sm:p-10 shadow-[0_20px_40px_-15px_rgba(0,0,0,0.8)] relative overflow-hidden group w-full">
      
      {/* Background glow accent */}
      <div className="absolute top-0 right-0 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl pointer-events-none" />

      <div className="relative z-10 space-y-8">
        
        {/* Header */}
        <div className="flex items-center justify-between border-b border-white/[0.08] pb-5">
          <h3 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight flex items-center gap-3">
            <span className="text-3xl">🤖</span> AI Career Analysis
          </h3>
          <span className="text-xs font-mono px-3 py-1.5 rounded-full bg-purple-500/10 text-purple-300 border border-purple-500/20">
            DEEP TELEMETRY
          </span>
        </div>

        {/* OVERALL FIT SCORE - Full Width & Prominent */}
        <div className="bg-zinc-900/80 border border-white/[0.08] rounded-2xl p-6 sm:p-8 backdrop-blur-md shadow-inner">
          <div className="flex justify-between items-center mb-4 font-mono">
            <span className="text-sm text-zinc-300 uppercase tracking-wider font-semibold">Overall Fit Telemetry</span>
            <span className="text-purple-400 font-extrabold text-2xl sm:text-3xl">
              {score}/100
            </span>
          </div>

          <div className="w-full bg-zinc-950 rounded-full h-3.5 overflow-hidden border border-white/[0.06] p-0.5">
            <div
              className="h-full bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 rounded-full shadow-[0_0_16px_rgba(168,85,247,0.6)] transition-all duration-700"
              style={{ width: `${score}%` }}
            />
          </div>
        </div>

        {/* Grid Layout for Sections to maximize space */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          {/* STRENGTHS */}
          {recommendation.strengths && recommendation.strengths.length > 0 && (
            <div className="bg-zinc-900/40 border border-white/[0.06] rounded-2xl p-6 flex flex-col justify-between">
              <div>
                <h4 className="font-mono text-xs uppercase tracking-wider text-emerald-400 mb-4 flex items-center gap-2 font-semibold">
                  <span className="text-base">💪</span> Core Strengths
                </h4>
                <div className="flex flex-wrap gap-2.5">
                  {recommendation.strengths.map((item) => (
                    <span
                      key={item}
                      className="bg-emerald-500/10 border border-emerald-500/20 text-emerald-300 px-3.5 py-2 rounded-xl text-xs font-mono"
                    >
                      ✅ {item}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* MISSING SKILLS */}
          {recommendation.missing_skills && recommendation.missing_skills.length > 0 && (
            <div className="bg-zinc-900/40 border border-white/[0.06] rounded-2xl p-6 flex flex-col justify-between">
              <div>
                <h4 className="font-mono text-xs uppercase tracking-wider text-red-400 mb-4 flex items-center gap-2 font-semibold">
                  <span className="text-base">❌</span> Missing Target Skills
                </h4>
                <div className="space-y-2">
                  {recommendation.missing_skills.map((skill) => (
                    <div key={skill} className="bg-zinc-950/60 border border-white/[0.04] px-3.5 py-2 rounded-xl text-xs font-mono text-red-300 flex items-center gap-2">
                      <span className="w-1.5 h-1.5 rounded-full bg-red-400" />
                      <span>{skill}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}

        </div>

        {/* SKILL GAP ANALYSIS - Full Width */}
        {recommendation.skill_gap && Object.keys(recommendation.skill_gap).length > 0 && (
          <div className="bg-zinc-900/40 border border-white/[0.06] rounded-2xl p-6 sm:p-8">
            <h4 className="font-mono text-xs uppercase tracking-wider text-amber-400 mb-6 flex items-center gap-2 font-semibold">
              <span className="text-base">📊</span> Skill Gap Telemetry
            </h4>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {Object.entries(recommendation.skill_gap).map(([skill, value]) => (
                <div key={skill} className="bg-zinc-950/60 border border-white/[0.04] rounded-xl p-4 space-y-2">
                  <div className="flex justify-between text-xs font-mono text-zinc-300">
                    <span className="font-medium">{skill}</span>
                    <span className="text-amber-400 font-bold">{value}%</span>
                  </div>
                  <div className="w-full bg-zinc-900 rounded-full h-2 overflow-hidden border border-white/[0.04]">
                    <div
                      className="bg-amber-400 h-full rounded-full shadow-[0_0_10px_rgba(251,191,36,0.4)] transition-all duration-500"
                      style={{ width: `${value}%` }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Grid Layout for Roadmaps & Refinement */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          {/* IMPROVEMENT PLAN */}
          {recommendation.improvement_suggestions && recommendation.improvement_suggestions.length > 0 && (
            <div className="bg-zinc-900/40 border border-white/[0.06] rounded-2xl p-6 flex flex-col justify-between">
              <div>
                <h4 className="font-mono text-xs uppercase tracking-wider text-indigo-400 mb-4 flex items-center gap-2 font-semibold">
                  <span className="text-base">🚀</span> Optimization Roadmap
                </h4>
                <ul className="space-y-2.5 text-xs font-mono text-zinc-300">
                  {recommendation.improvement_suggestions.map((item) => (
                    <li key={item} className="bg-zinc-950/60 border border-white/[0.04] p-3 rounded-xl text-zinc-200 flex items-start gap-2">
                      <span className="text-indigo-400 font-bold">→</span>
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          )}

          {/* REDUNDANT CONTENT */}
          {recommendation.redundant_content && recommendation.redundant_content.length > 0 && (
            <div className="bg-zinc-900/40 border border-white/[0.06] rounded-2xl p-6 flex flex-col justify-between">
              <div>
                <h4 className="font-mono text-xs uppercase tracking-wider text-zinc-400 mb-4 flex items-center gap-2 font-semibold">
                  <span className="text-base">🗑</span> Redundant / Refine Targets
                </h4>
                <ul className="space-y-2.5 text-xs font-mono text-zinc-400">
                  {recommendation.redundant_content.map((item) => (
                    <li key={item} className="bg-zinc-950/60 border border-white/[0.04] p-3 rounded-xl text-zinc-400 flex items-start gap-2">
                      <span className="text-zinc-500 font-bold">-</span>
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          )}

        </div>

        {/* AI JUSTIFICATION - Full Width */}
        {recommendation.justification && (
          <div className="bg-zinc-900/80 border border-white/[0.08] rounded-2xl p-6 sm:p-8 backdrop-blur-md">
            <h4 className="font-mono text-xs uppercase tracking-wider text-zinc-200 mb-3 flex items-center gap-2 font-semibold">
              <span className="text-base">💡</span> Neural Explanation
            </h4>
            <p className="text-sm font-mono text-zinc-300 leading-relaxed">
              {recommendation.justification}
            </p>
          </div>
        )}

      </div>
    </div>
  );
}

export default RecommendationCard;