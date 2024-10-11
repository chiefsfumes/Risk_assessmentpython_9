import os
import logging
from typing import Dict, NamedTuple

class Scenario(NamedTuple):
    name: str
    temp_increase: float
    carbon_price: float
    renewable_energy: float
    policy_stringency: float
    biodiversity_loss: float
    ecosystem_degradation: float
    financial_stability: float
    supply_chain_disruption: float
    biodiversity_index: float  # New parameter
    ecosystem_health: float  # New parameter
    financial_system_stability: float  # New parameter
    global_supply_chain_resilience: float  # New parameter

# Scenario definitions
SCENARIOS: Dict[str, Scenario] = {
    "Net Zero 2050": Scenario(
        name="Net Zero 2050",
        temp_increase=1.5,
        carbon_price=250,
        renewable_energy=0.75,
        policy_stringency=0.9,
        biodiversity_loss=0.1,
        ecosystem_degradation=0.2,
        financial_stability=0.8,
        supply_chain_disruption=0.3,
        biodiversity_index=0.9,
        ecosystem_health=0.8,
        financial_system_stability=0.85,
        global_supply_chain_resilience=0.7
    ),
    "Delayed Transition": Scenario(
        name="Delayed Transition",
        temp_increase=2.5,
        carbon_price=125,
        renewable_energy=0.55,
        policy_stringency=0.6,
        biodiversity_loss=0.3,
        ecosystem_degradation=0.4,
        financial_stability=0.6,
        supply_chain_disruption=0.5,
        biodiversity_index=0.7,
        ecosystem_health=0.6,
        financial_system_stability=0.7,
        global_supply_chain_resilience=0.6
    ),
    "Current Policies": Scenario(
        name="Current Policies",
        temp_increase=3.5,
        carbon_price=35,
        renewable_energy=0.35,
        policy_stringency=0.2,
        biodiversity_loss=0.5,
        ecosystem_degradation=0.6,
        financial_stability=0.4,
        supply_chain_disruption=0.7,
        biodiversity_index=0.5,
        ecosystem_health=0.4,
        financial_system_stability=0.5,
        global_supply_chain_resilience=0.4
    ),
    "Nature Positive": Scenario(
        name="Nature Positive",
        temp_increase=1.8,
        carbon_price=200,
        renewable_energy=0.7,
        policy_stringency=0.8,
        biodiversity_loss=-0.1,  # Net gain
        ecosystem_degradation=-0.2,  # Net restoration
        financial_stability=0.75,
        supply_chain_disruption=0.4,
        biodiversity_index=0.95,
        ecosystem_health=0.9,
        financial_system_stability=0.8,
        global_supply_chain_resilience=0.75
    ),
    "Systemic Crisis": Scenario(
        name="Systemic Crisis",
        temp_increase=4.0,
        carbon_price=50,
        renewable_energy=0.4,
        policy_stringency=0.3,
        biodiversity_loss=0.6,
        ecosystem_degradation=0.7,
        financial_stability=0.2,
        supply_chain_disruption=0.8,
        biodiversity_index=0.3,
        ecosystem_health=0.2,
        financial_system_stability=0.1,
        global_supply_chain_resilience=0.2
    )
}

# Keep existing content below this line