# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 12:24:35 2025

@author: mario
"""

# ==============================================================================
#           THE COMPLETE STOCHASTIC SYSTEM: A MODEL OF THOUGHT
#
#   This code is the final result of our conversation. It represents a system
#   that can learn, reason, and creatively explore ideas based on a set of
#   core beliefs (Axioms).
#
#   - Author of the Logic & Vision: Mario Guzman
#   - Coded by: Gemini, and Mario Guzman 
# ==============================================================================

import sympy
import random

# ==============================================================================
# CLASS 1: SymbolicSystemV2 (The Base Class with Cognitive Skills)
#
# This is the foundation. It knows how to learn facts and has a toolbox of
# skills like solving, simplifying, and verifying.
# ==============================================================================
class SymbolicSystemV2:
    """The base system with a toolbox of cognitive skills."""
    def __init__(self, name):
        self.name = name
        self.variables = set()
        self.known_truths = []
        print(f"--- Advanced Symbolic Brain '{self.name}' Initialized ---")

    def __repr__(self):
        """Provides a string representation of the brain's current state."""
        state = f"\n--- State of Brain '{self.name}' ---\n"
        state += f"Known Variables: {sorted(list(self.variables), key=str)}\n"
        state += "Known Truths (Formulas):\n"
        for i, truth in enumerate(self.known_truths):
            state += f"  [{i}]: {truth}\n"
        return state

    def add_truth(self, equation_text):
        """Learns a new fact from a string like 'c = a + b'."""
        try:
            equation = sympy.sympify(f"Eq({equation_text.replace('=', ',')})", locals=globals())
            self.known_truths.append(equation)
            for atom in equation.free_symbols:
                self.variables.add(atom)
            print(f"Learned new truth: {equation}")
        except Exception as e:
            print(f"Error learning '{equation_text}': {e}")

    def solve_for(self, variable_symbol):
        """Skill 1: Solves for a variable using its knowledge."""
        print(f"\n> Attempting to solve for variable '{variable_symbol}'...")
        for i, truth in enumerate(self.known_truths):
            if variable_symbol in truth.free_symbols:
                try:
                    solutions = sympy.solve(truth, variable_symbol)
                    if solutions:
                        print(f"  > Success! Using Truth [{i}], found that '{variable_symbol}' can be expressed as: {solutions[0]}")
                        return solutions[0]
                except Exception:
                    continue
        print(f"  > Failure. Could not find a way to express '{variable_symbol}'.")
        return None

    def simplify_truth(self, truth_index):
        """Skill 2: Refines a known truth into its simplest form."""
        print(f"\n> Simplifying Truth [{truth_index}]...")
        if truth_index >= len(self.known_truths):
            print("  > Failure. That truth index does not exist.")
            return
        original_truth = self.known_truths[truth_index]
        simplified_truth = sympy.simplify(original_truth)
        self.known_truths[truth_index] = simplified_truth
        print(f"  > Refined '{original_truth}' into '{simplified_truth}'.")

    def verify_hypothesis(self, hypothesis_text):
        """Skill 3: Checks if a new idea is consistent with its knowledge."""
        print(f"\n> Verifying hypothesis: '{hypothesis_text}'...")
        try:
            hypothesis = sympy.sympify(f"Eq({hypothesis_text.replace('=', ',')})", locals=globals())
        except Exception as e:
            print(f"  > Invalid hypothesis format: {e}")
            return False
        temp_hypothesis = hypothesis
        for truth in self.known_truths:
            temp_hypothesis = sympy.simplify(temp_hypothesis.subs(truth.lhs, truth.rhs))
        if temp_hypothesis == True:
            print(f"  > Verdict: The hypothesis is TRUE based on my current knowledge.")
            return True
        else:
            print(f"  > Verdict: The hypothesis is FALSE or cannot be proven.")
            return False

# ==============================================================================
# CLASS 2: AxiomaticSystem (Inherits from V2, Adds Axioms)
#
# This brain understands the concept of an Axiom - a foundational belief
# that cannot be questioned and is the ultimate source of truth.
# ==============================================================================
class AxiomaticSystem(SymbolicSystemV2):
    """An axiomatic reasoner that builds its logic on unquestionable beliefs."""
    def __init__(self, name):
        super().__init__(name)
        self.axioms = []
        print(f"*** Axiomatic Engine engaged. System can now accept foundational beliefs. ***")

    def __repr__(self):
        state = super().__repr__()
        state += "Axiomatic Truths (Foundational Beliefs):\n"
        for i, axiom in enumerate(self.axioms):
            state += f"  [A{i}]: {axiom}\n"
        return state

    def accept_as_axiom(self, axiom_text):
        """Forces a belief into the system's core knowledge."""
        print(f"\n>>> Accepting AXIOM: '{axiom_text}'")
        try:
            axiom = sympy.sympify(f"Eq({axiom_text.replace('=', ',')})", locals=globals())
            self.axioms.append(axiom)
            for atom in axiom.free_symbols:
                self.variables.add(atom)
        except Exception as e:
            print(f"Error accepting axiom '{axiom_text}': {e}")

    def verify_hypothesis(self, hypothesis_text):
        """Upgraded Guardian of Logic that respects Axioms above all else."""
        print(f"\n> Verifying hypothesis against all truths AND axioms: '{hypothesis_text}'...")
        try:
            hypothesis = sympy.sympify(f"Eq({hypothesis_text.replace('=', ',')})", locals=globals())
        except Exception as e:
            print(f"  > Invalid hypothesis format: {e}")
            return False
        temp_hypothesis = hypothesis
        # Guardian must use unquestionable axioms first
        for axiom in self.axioms:
            temp_hypothesis = sympy.simplify(temp_hypothesis.subs(axiom.lhs, axiom.rhs))
        # Then it uses the normal, derived truths
        for truth in self.known_truths:
            temp_hypothesis = sympy.simplify(temp_hypothesis.subs(truth.lhs, truth.rhs))
        if temp_hypothesis == True:
            print(f"  > Verdict: The hypothesis is TRUE based on my total worldview.")
            return True
        else:
            print(f"  > Verdict: The hypothesis is FALSE or cannot be proven.")
            return False

# ==============================================================================
# CLASS 3: StochasticSystem (Inherits from Axiomatic, Adds Creativity)
#
# The final form. This system has a chance to take a "shot in the dark"
# by exploring a random, unproven "dummy idea" to see if it unlocks new truths.
# ==============================================================================
class StochasticSystem(AxiomaticSystem):
    """The final system. A logical reasoner that can have flashes of creative insight."""
    def __init__(self, name, dummy_idea_chance=0.25):
        super().__init__(name)
        self.dummy_idea_chance = dummy_idea_chance
        print(f"%%%% Stochastic Insight Engine enabled with a {self.dummy_idea_chance*100}% chance. %%%%")

    def add_truth(self, equation_text):
        """Overrides parent to prevent learning duplicate or trivial facts."""
        try:
            new_truth = sympy.sympify(f"Eq({equation_text.replace('=', ',')})", locals=globals())
            if new_truth in self.known_truths or new_truth in self.axioms or sympy.simplify(new_truth) == True:
                print(f"(Skipping known or trivial fact: {new_truth})")
                return
            super().add_truth(equation_text)
        except Exception as e:
            print(f"Error learning '{equation_text}': {e}")

    def explore_dummy_idea(self):
        """The 'long-shot' or 'flash of insight' skill."""
        print("\n    ~~~~~~ A 'Shot in the Dark' ~~~~~~")
        if len(self.variables) < 2: return
        var1, var2 = random.sample(list(self.variables), 2)
        dummy_hypothesis = sympy.Eq(var1, var2)
        print(f"    Let's try a crazy idea... What if '{dummy_hypothesis}' was true, just for a moment?")
        if not self.known_truths and not self.axioms: return
        truth_to_test = random.choice(self.known_truths + self.axioms)
        print(f"    Let's see how this affects my belief: '{truth_to_test}'")
        new_consequence = sympy.simplify(truth_to_test.subs(dummy_hypothesis.lhs, dummy_hypothesis.rhs))
        print(f"    If my crazy idea were true, it would imply that: '{new_consequence}'")
        if self.verify_hypothesis(str(new_consequence).replace("Eq(","").replace(")","")):
            print("    <<<<< EUREKA! The consequence is logically valid! >>>>>")
            print("    My crazy idea led to a real discovery!")
            self.add_truth(str(new_consequence).replace("Eq(","").replace(")",""))
        else:
            print("    (As expected, the crazy idea led nowhere. Discarding.)")
            
    def think_for_itself(self, num_thoughts):
        """The main thinking loop, combining logic with creative leaps."""
        print(f"\n--- {self.name} is starting a STOCHASTIC thinking session for {num_thoughts} cycles... ---")
        for i in range(num_thoughts):
            print(f"\n[Stochastic Cycle {i+1}/{num_thoughts}]")
            if random.random() < self.dummy_idea_chance:
                self.explore_dummy_idea()
            else:
                print("  > Performing routine logical exploration...")
                if len(self.known_truths) + len(self.axioms) < 2: continue
                # Logic: Try to connect two ideas
                all_knowledge = self.known_truths + self.axioms
                truth1, truth2 = random.sample(all_knowledge, 2)
                common_vars = truth1.free_symbols.intersection(truth2.free_symbols)
                if not common_vars: continue
                var_to_sub = list(common_vars)[0]
                sub_expression = sympy.solve(truth1, var_to_sub)
                if not sub_expression: continue
                hypothesis = sympy.simplify(truth2.subs(var_to_sub, sub_expression[0]))
                if self.verify_hypothesis(str(hypothesis).replace("Eq(","").replace(")","")):
                    self.add_truth(str(hypothesis).replace("Eq(","").replace(")",""))

# ==============================================================================
#                               THE MAIN PROGRAM
#                     This is where we run our experiments.
# ==============================================================================
if __name__ == "__main__":

    # --- Define the variables the brain can understand ---
    a, b, c, result = sympy.symbols('a b c result')

    # --- Step 1: Create our final, most advanced brain ---
    final_brain = StochasticSystem(name="The Innovator", dummy_idea_chance=0.4) # 40% chance of a 'crazy idea'

    # --- Step 2: Teach it the foundational axioms of a simple world ---
    print("\n--- TEACHING THE BRAIN THE AXIOMS OF ITS UNIVERSE ---")
    final_brain.accept_as_axiom("result = a*b + c")
    final_brain.accept_as_axiom("b = a")
    final_brain.accept_as_axiom("c = a")

    # --- Step 3: See the initial state ---
    print("\n--- INITIAL STATE OF KNOWLEDGE ---")
    print(final_brain)

    # --- Step 4: Let it think! ---
    # It will now mix normal logical thought with occasional "shots in the dark".
    # Can it discover the final, simplified relationship between 'result' and 'a'?
    final_brain.think_for_itself(num_thoughts=10)

    # --- Step 5: The Final State of Knowledge ---
    print("\n\n--- THE FINAL WORLDVIEW AFTER THINKING ---")
    print("Let's see if the brain discovered the final connection 'result = a**2 + a':")
    print(final_brain)

