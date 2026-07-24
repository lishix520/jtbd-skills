#!/usr/bin/env python3
"""
JTBD Opportunity Calculator Script

Calculates Outcome-Driven Innovation (ODI) Opportunity Scores from survey JSON inputs
according to the jtbd-opportunity-calculator specification.
"""

import json
import sys
from typing import Dict, Any, List


def classify_opportunity(opp_score: float) -> str:
    if opp_score >= 15.0:
        return "extreme_underserved"
    elif opp_score >= 12.0:
        return "high_underserved"
    elif opp_score >= 10.0:
        return "moderate_underserved"
    elif opp_score >= 8.0:
        return "appropriately_served"
    else:
        return "overserved_candidate"


def calculate_opportunity(survey_data: Dict[str, Any]) -> Dict[str, Any]:
    meta = survey_data.get("survey_metadata", {})
    outcomes = survey_data.get("outcomes", [])
    
    importance_scale = meta.get("importance_scale", "1_to_10")
    satisfaction_scale = meta.get("satisfaction_scale", "1_to_10")
    sample_size = meta.get("sample_size", 0)
    collection_method = meta.get("collection_method", "")
    
    data_limitations: List[str] = []
    
    # Check scale validity (v0.1 strictly requires matching 1_to_10 scales)
    if importance_scale != "1_to_10" or satisfaction_scale != "1_to_10":
        return {
            "survey_metadata": meta,
            "data_quality_status": "invalid",
            "calculation_status": "blocked",
            "data_limitations": [
                "Unsupported scale: v0.1 requires matching 1_to_10 importance and satisfaction scales."
            ],
            "results": []
        }
    
    # Check if outcomes present
    if not outcomes:
        limitations = ["Missing numerical data: No outcome ratings provided."]
        if survey_data.get("text_feedback"):
            limitations.append("Qualitative text feedback was not converted into numerical ratings.")
            
        return {
            "survey_metadata": meta,
            "data_quality_status": "incomplete",
            "calculation_status": "blocked",
            "data_limitations": limitations,
            "results": []
        }

    # Assess methodology
    sample_size_status = "adequate" if sample_size >= 100 else ("small" if sample_size > 0 else "unknown")
    if sample_size < 100:
        data_limitations.append(f"Sample size N = {sample_size} (< 100); results represent exploratory hypotheses.")
    
    coll_status = "reported" if collection_method else "missing"
    if not collection_method:
        data_limitations.append("Collection method missing.")
        
    methodological_assessment = {
        "sample_size_status": sample_size_status,
        "representativeness": "unverified",
        "collection_method_status": coll_status
    }
    
    results = []
    total_count = len(outcomes)
    underserved_count = 0
    appropriately_served_count = 0
    overserved_count = 0
    
    for item in outcomes:
        imp = item.get("importance_mean")
        sat = item.get("satisfaction_mean")
        
        if imp is None or sat is None or not isinstance(imp, (int, float)) or not isinstance(sat, (int, float)):
            return {
                "survey_metadata": meta,
                "data_quality_status": "incomplete",
                "calculation_status": "blocked",
                "data_limitations": ["Missing numerical data: Ratings must be valid numbers."],
                "results": []
            }
            
        imp_val = float(imp)
        sat_val = float(sat)
        
        # Check out-of-bounds ratings
        if not (1.0 <= imp_val <= 10.0) or not (1.0 <= sat_val <= 10.0):
            return {
                "survey_metadata": meta,
                "data_quality_status": "invalid",
                "calculation_status": "blocked",
                "data_limitations": [
                    "Out-of-bounds rating: importance_mean and satisfaction_mean must be within 1.0 to 10.0."
                ],
                "results": []
            }
        
        gap = round(max(imp_val - sat_val, 0.0), 2)
        opp = round(imp_val + gap, 2)
        
        if sat_val > imp_val:
            sat_rel = "above_importance"
        elif sat_val == imp_val:
            sat_rel = "matches_importance"
        else:
            sat_rel = "below_importance"
            
        classification = classify_opportunity(opp)
        overserved_signal = (opp < 8.0) and (sat_val > imp_val)
        
        if "underserved" in classification:
            underserved_count += 1
        elif classification == "appropriately_served":
            appropriately_served_count += 1
        else:
            overserved_count += 1
            
        results.append({
            "id": item.get("id", ""),
            "statement": item.get("statement", ""),
            "importance_mean": imp_val,
            "satisfaction_mean": sat_val,
            "satisfaction_gap": round(gap, 2),
            "satisfaction_relation": sat_rel,
            "opportunity_score": round(opp, 2),
            "classification": classification,
            "overserved_signal": overserved_signal,
            "segment": item.get("segment", "")
        })
        
    return {
        "survey_metadata": meta,
        "data_quality_status": "complete",
        "calculation_status": "completed",
        "methodological_assessment": methodological_assessment,
        "scale_handling": {
            "calculation_scale": importance_scale,
            "normalization": "none",
            "threshold_interpretation": "standard"
        },
        "calculation_summary": {
            "total_outcomes_evaluated": total_count,
            "underserved_count": underserved_count,
            "appropriately_served_count": appropriately_served_count,
            "overserved_count": overserved_count
        },
        "data_limitations": data_limitations,
        "results": results
    }


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)
        
    output = calculate_opportunity(data)
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
