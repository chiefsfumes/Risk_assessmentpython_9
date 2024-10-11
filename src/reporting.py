import json
import numpy as np
from typing import List, Dict, Tuple
import pandas as pd
import os
from src.models import Risk, RiskInteraction, SimulationResult, Scenario
from src.config import OUTPUT_DIR

def generate_report(risks: List[Risk], categorized_risks: Dict[str, List[Risk]], 
                    risk_interactions: List[RiskInteraction], scenario_impacts: Dict[str, List[Tuple[Risk, float]]],
                    simulation_results: Dict[str, Dict[int, SimulationResult]], clustered_risks: Dict[int, List[int]],
                    risk_entities: Dict[str, List[str]], sensitivity_results: Dict[str, Dict[str, float]],
                    time_series_results: Dict[int, List[float]], scenarios: Dict[str, Scenario],
                    advanced_analysis: Dict, systemic_risks: Dict, trigger_points: Dict,
                    resilience_assessment: Dict, monte_carlo_results: Dict,
                    aggregate_impact: Dict, tipping_points: List[Dict]) -> str:
    report = {
        "executive_summary": generate_executive_summary(risks, scenario_impacts, simulation_results, advanced_analysis, aggregate_impact, tipping_points),
        "risk_overview": {
            "total_risks": len(risks),
            "risk_categories": {category: len(risks) for category, risks in categorized_risks.items()},
            "high_impact_risks": [risk.to_dict() for risk in risks if risk.impact > 0.7],
        },
        "risk_interactions": {
            "summary": summarize_risk_interactions(risk_interactions),
            "detailed_interactions": [interaction.__dict__ for interaction in risk_interactions]
        },
        "scenario_analysis": {
            scenario: {
                "summary": summarize_scenario_impact(impacts),
                "detailed_impacts": [
                    {"risk_id": risk.id, "impact": impact} 
                    for risk, impact in sorted(impacts, key=lambda x: x[1], reverse=True)
                ],
                "llm_analysis": advanced_analysis["comprehensive_analysis"][scenario]
            } for scenario, impacts in scenario_impacts.items()
        },
        "monte_carlo_results": {
            scenario: {
                risk_id: {
                    "mean_impact": np.mean(results.impact_distribution),
                    "std_impact": np.std(results.impact_distribution),
                    "5th_percentile_impact": np.percentile(results.impact_distribution, 5),
                    "95th_percentile_impact": np.percentile(results.impact_distribution, 95),
                    "mean_likelihood": np.mean(results.likelihood_distribution),
                    "std_likelihood": np.std(results.likelihood_distribution)
                } for risk_id, results in scenario_results.items()
            } for scenario, scenario_results in simulation_results.items()
        },
        "risk_clusters": clustered_risks,
        "risk_entities": risk_entities,
        "sensitivity_analysis": sensitivity_results,
        "time_series_projection": {risk_id: projections for risk_id, projections in time_series_results.items()},
        "risk_narratives": advanced_analysis["risk_narratives"],
        "executive_insights": advanced_analysis["executive_insights"],
        "mitigation_strategies": generate_mitigation_strategies(risks, scenario_impacts, simulation_results),
        "systemic_risks": systemic_risks,
        "trigger_points": trigger_points,
        "resilience_assessment": resilience_assessment,
        "aggregate_impact": aggregate_impact,
        "tipping_points": tipping_points
    }
    
    report_json = json.dumps(report, indent=2)
    
    with open(os.path.join(OUTPUT_DIR, 'climate_risk_report.json'), 'w') as f:
        f.write(report_json)
    
    generate_html_report(report)
    
    return report_json

# Keep existing functions

def generate_executive_summary(risks: List[Risk], scenario_impacts: Dict[str, List[Tuple[Risk, float]]], 
                               simulation_results: Dict[str, Dict[int, SimulationResult]],
                               advanced_analysis: Dict, aggregate_impact: Dict, tipping_points: List[Dict]) -> str:
    num_risks = len(risks)
    high_impact_risks = sum(1 for risk in risks if risk.impact > 0.7)
    worst_scenario = max(scenario_impacts.items(), key=lambda x: sum(impact for _, impact in x[1]))
    
    summary = f"""
    Executive Summary:
    
    This climate risk assessment identified {num_risks} distinct risks, with {high_impact_risks} classified as high-impact.
    The '{worst_scenario[0]}' scenario presents the most significant challenges, with potential for severe impacts across multiple risk categories.
    
    Key findings:
    1. {summarize_top_risks(scenario_impacts[worst_scenario[0]])}
    2. {summarize_monte_carlo_results(simulation_results)}
    3. Aggregate Impact: The mean aggregate impact across all risks is {aggregate_impact['mean']:.2f}, with a 95th percentile impact of {aggregate_impact['95th_percentile']:.2f}.
    4. Tipping Points: {len(tipping_points)} potential tipping points were identified, with the most critical occurring at an impact level of {max(tp['tipping_point_level'] for tp in tipping_points):.2f}.
    
    Advanced Analysis Insights:
    {advanced_analysis['executive_insights']}
    
    Immediate attention is required to develop and implement comprehensive mitigation strategies, particularly focusing on the high-impact risks and potential tipping points identified in this assessment.
    """
    
    return summary

# Keep existing functions and add any new ones as needed

def generate_html_report(report: Dict) -> None:
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Climate Risk Assessment Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
            h1, h2, h3 {{ color: #2c3e50; }}
            .summary {{ background-color: #f0f0f0; padding: 15px; border-radius: 5px; }}
            .risk-category {{ margin-bottom: 20px; }}
            .scenario {{ margin-bottom: 30px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>Climate Risk Assessment Report</h1>
        
        <div class="summary">
            <h2>Executive Summary</h2>
            <p>{report['executive_summary']}</p>
        </div>
        
        <h2>Risk Overview</h2>
        <p>Total Risks: {report['risk_overview']['total_risks']}</p>
        <h3>Risk Categories</h3>
        <ul>
            {' '.join(f'<li>{category}: {count}</li>' for category, count in report['risk_overview']['risk_categories'].items())}
        </ul>
        
        <h3>High Impact Risks</h3>
        <ul>
            {' '.join(f'<li>Risk {risk["id"]}: {risk["description"]} (Impact: {risk["impact"]})</li>' for risk in report['risk_overview']['high_impact_risks'])}
        </ul>
        
        <h2>Scenario Analysis</h2>
        {' '.join(f'''
        <div class="scenario">
            <h3>{scenario}</h3>
            <p>{data['summary']}</p>
            <h4>Top 3 Risks:</h4>
            <ul>
                {' '.join(f'<li>Risk {impact["risk_id"]}: Impact {impact["impact"]:.2f}</li>' for impact in data['detailed_impacts'][:3])}
            </ul>
            <h4>LLM Analysis:</h4>
            {' '.join(f'<p>{analysis}</p>' for analysis in data['llm_analysis'].values())}
        </div>
        ''' for scenario, data in report['scenario_analysis'].items())}
        
        <h2>Monte Carlo Simulation Results</h2>
        {' '.join(f'''
        <h3>{scenario}</h3>
        <table>
            <tr>
                <th>Risk ID</th>
                <th>Mean Impact</th>
                <th>Std Dev Impact</th>
                <th>5th Percentile</th>
                <th>95th Percentile</th>
            </tr>
            {' '.join(f'''
            <tr>
                <td>{risk_id}</td>
                <td>{results['mean_impact']:.2f}</td>
                <td>{results['std_impact']:.2f}</td>
                <td>{results['5th_percentile_impact']:.2f}</td>
                <td>{results['95th_percentile_impact']:.2f}</td>
            </tr>
            ''' for risk_id, results in scenario_results.items())}
        </table>
        ''' for scenario, scenario_results in report['monte_carlo_results'].items())}
        
        <h2>Sensitivity Analysis</h2>
        <table>
            <tr>
                <th>Scenario</th>
                {' '.join(f'<th>{variable}</th>' for variable in next(iter(report['sensitivity_analysis'].values())).keys())}
            </tr>
            {' '.join(f'''
            <tr>
                <td>{scenario}</td>
                {' '.join(f'<td>{sensitivity:.2f}</td>' for sensitivity in sensitivities.values())}
            </tr>
            ''' for scenario, sensitivities in report['sensitivity_analysis'].items())}
        </table>
        
        <h2>Risk Narratives</h2>
        {' '.join(f'''
        <div class="risk-category">
            <h3>Risk {risk_id}</h3>
            <p>{narrative}</p>
        </div>
        ''' for risk_id, narrative in report['risk_narratives'].items())}
        
        <h2>Executive Insights</h2>
        <p>{report['executive_insights']}</p>
        
        <h2>Mitigation Strategies</h2>
        {' '.join(f'''
        <div class="risk-category">
            <h3>Risk {risk_id}</h3>
            <ul>
                {' '.join(f'<li>{strategy}</li>' for strategy in strategies)}
            </ul>
        </div>
        ''' for risk_id, strategies in report['mitigation_strategies'].items())}
        
        <h2>Systemic Risks</h2>
        <ul>
            {' '.join(f'<li>Risk {risk_id}: {risk_info["description"]} (Impact: {risk_info["impact"]:.2f}, Systemic Factor: {risk_info["systemic_factor"]})</li>' for risk_id, risk_info in report['systemic_risks'].items())}
        </ul>
        
        <h2>Trigger Points</h2>
        <ul>
            {' '.join(f'<li>Risk {risk_id}: {trigger_info["description"]} (Centrality: {trigger_info["centrality"]:.2f}, Connected Risks: {", ".join(map(str, trigger_info["connected_risks"]))})</li>' for risk_id, trigger_info in report['trigger_points'].items())}
        </ul>
        
        <h2>Resilience Assessment</h2>
        <table>
            <tr>
                <th>Metric</th>
                <th>Value</th>
            </tr>
            {' '.join(f'''
            <tr>
                <td>{metric}</td>
                <td>{value:.2f}</td>
            </tr>
            ''' for metric, value in report['resilience_assessment'].items())}
        </table>
        
        <h2>Aggregate Impact</h2>
        <ul>
            <li>Mean: {report['aggregate_impact']['mean']:.2f}</li>
            <li>Median: {report['aggregate_impact']['median']:.2f}</li>
            <li>95th Percentile: {report['aggregate_impact']['95th_percentile']:.2f}</li>
            <li>Max: {report['aggregate_impact']['max']:.2f}</li>
        </ul>
        
        <h2>Tipping Points</h2>
        <ul>
            {' '.join(f'<li>Risk {tp["risk_id"]}: {tp["risk_description"]} (Tipping Point Level: {tp["tipping_point_level"]:.2f}, Aggregate Impact: {tp["aggregate_impact"]:.2f})</li>' for tp in report['tipping_points'])}
        </ul>
        
    </body>
    </html>
    """
    
    with open(os.path.join(OUTPUT_DIR, 'climate_risk_report.html'), 'w') as f:
        f.write(html_content)