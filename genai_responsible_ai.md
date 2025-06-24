# Responsible generative AI

It defines a 4-stage process (the "4M" process):
1. **Map** potential harms.
Generated content might:
- be offensive, pejorative (abusive), or discriminatory (biased).
- contain factual inaccuracies.
- encourage or support illegal/unethical behaviour or practices.

The [information and guidelines](https://learn.microsoft.com/en-us/azure/ai-services/responsible-use-of-ai-overview) can help identify potential harms.

2. **Measure** the presence of these harms in the generated outputs.
- Assess the likelihood of the occurrence of the harms and the resulting level of impact if it does.
- Then prioritize the most likely and impactful harms first.

3. **Mitigate** the harms at multiple layers, to minimize their presence and impact. Ensure transparent communication about potential risks to users.
- Test to verify that the harms occur and the conditions to occur.
- The testing might also reveal the presence of previously unidentified harms.

4. **Manage** the solution responsibly by defining/following a deployment and operational readiness plan.
- Document the details and share them with the stakeholders.
- Maintain and further update the list of harms.

The stages are connected as:

(1) Identify potential harms -> (2) prioritize identified harms -> (3) Test/verify the prioritized harms -> (4) Document and share the verified harms

## Measure potential harms
Generalized approach:
- Prepare a diverse selection of input prompts that are likely to result in each potential harm.
- Generate output from each prompt.
- Evaluate the output based on pre-defined criteria (may be as simple as "harmful" or "not harmful").

The measurement result should be documented and shared with stakeholders.

In most scenarios, we should start by manually testing and evaluating on a small set of prompts.

Then apply automated testing/measurement with a larger volume of test cases. The automated solution may include the use of a classification model to evaluate the output.

Even after the automated solution is implemented, we should periodically perform manual testing to validate new scenarios and ensure that the automated solution is working properly.

## Mitigate potential harms

Mitigation techniques can be applied at each of four layers:

1. The model layer
- Selecting model that is appropriate for the intended solution use.
- Fine-tuning a foundation model with your own dataset.

2. The safety system layer
- Platform-level configurations and capabilities. For example, Azure AI Foundry supports content filtering on the generated output, classifies into four severity levels (safe, low, medium, and high), for 4 categories of potential harms (hate, sexual, violence, and self-harm).
- Can apply other detection algorithms to determine the presence of harms in the generated outputs.

3. The system message and grounding layer
- Specifying system message to define the model behavior.
- Applying prompt engineering techniques, add grounding data to input prompts.
- Using RAG.

4. The user experience layer
- Describe and document the capabilities and limitations of the system to stakeholders.

## Manage a responsible generative AI solution

Conduct prerelease compliance reviews on: Legal, Privacy, Security, Accessibility.

Release guidelines:
- Deliver in phrases to groups of users.
- Create an incident response plan.
- Create a rollback plan.
- Implement the capability to immediately block harmful system responses.
- Implement a capability to block specific users/apps/IPs in the event of system misuse.
- Implement a way for providing feedback and report issues.
- Track telemetry data to determine user satisfaction and identify functional gaps of usability challenges.

The Azure AI Foundry Content Safety provides features to keep AI safe from risk:
- Prompt shields: Scans for risks of user input attacks.
- Groundessness detection: Detects if text responses are grounded in a user's source content.
- Protected material detection: Scans for known copyrighted content.
- Custom categories: Define custom categories.