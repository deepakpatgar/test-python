import matplotlib.pyplot as plt
from tabulate import tabulate
from PIL import Image

# Enhanced brain functions data including frequency, data processing, neurons, and synapses
# Enhanced functions dictionary with additional brain function categories
functions = {
    'Sight': {
        'Brain Parts': ['Visual cortex', 'Visual association area', 'Occipital lobe'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Processing visual information',
        'Brain Waves': ['Alpha waves'],
        'Frequency': '40 Hz',
        'Data Processing (Short Term)': 'High',
        'Data Processing (Long Term)': 'Moderate',
        'Neurons': 'Hundreds of millions',
        'Synapses': 'Billions'
    },
    'Hearing': {
        'Brain Parts': ['Auditory cortex', 'Auditory association area', 'Temporal lobe'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Processing auditory information',
        'Brain Waves': ['Theta waves'],
        'Frequency': '20-30 Hz',
        'Data Processing (Short Term)': 'Moderate',
        'Data Processing (Long Term)': 'Low',
        'Neurons': 'Tens of millions',
        'Synapses': 'Hundreds of millions'
    },
    'Sensory': {
        'Brain Parts': ['Various sensory cortices', 'Thalamus', 'Parietal lobe'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Processing sensory inputs',
        'Brain Waves': ['Beta waves'],
        'Frequency': '15-30 Hz',
        'Data Processing (Short Term)': 'High',
        'Data Processing (Long Term)': 'Moderate',
        'Neurons': 'Hundreds of millions',
        'Synapses': 'Billions'
    },
    'Language': {
        'Brain Parts': ['Broca\'s area', 'Wernicke\'s area', 'Angular gyrus'],
        'Locations': ['Left hemisphere (dominant)'],
        'Functionality': 'Language processing and comprehension',
        'Brain Waves': ['Theta waves'],
        'Frequency': '5-8 Hz',
        'Data Processing (Short Term)': 'High',
        'Data Processing (Long Term)': 'Moderate',
        'Neurons': 'Tens of millions',
        'Synapses': 'Hundreds of millions'
    },
    'Cognition': {
        'Brain Parts': ['Prefrontal cortex', 'Temporal lobe', 'Parietal lobe'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Higher cognitive functions (thinking, reasoning)',
        'Brain Waves': ['Alpha waves', 'Beta waves'],
        'Frequency': '8-12 Hz (Alpha), 12-30 Hz (Beta)',
        'Data Processing (Short Term)': 'High',
        'Data Processing (Long Term)': 'High',
        'Neurons': 'Billions',
        'Synapses': 'Trillions'
    },
    'Action': {
        'Brain Parts': ['Motor cortex', 'Premotor cortex', 'Basal ganglia'],
        'Locations': ['Left hemisphere controls right side'],
        'Functionality': 'Initiating and coordinating voluntary movements',
        'Brain Waves': ['Beta waves'],
        'Frequency': '13-30 Hz',
        'Data Processing (Short Term)': 'Moderate',
        'Data Processing (Long Term)': 'Low',
        'Neurons': 'Hundreds of millions',
        'Synapses': 'Billions'
    },
    'Analysis': {
        'Brain Parts': ['Frontal lobe', 'Parietal lobe', 'Temporal lobe'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Analytical thinking and problem-solving',
        'Brain Waves': ['Beta waves', 'Gamma waves'],
        'Frequency': '13-30 Hz (Beta), 30-100 Hz (Gamma)',
        'Data Processing (Short Term)': 'High',
        'Data Processing (Long Term)': 'High',
        'Neurons': 'Billions',
        'Synapses': 'Trillions'
    },
    'Motor': {
        'Brain Parts': ['Motor cortex', 'Premotor cortex', 'Cerebellum'],
        'Locations': ['Left hemisphere controls right side'],
        'Functionality': 'Control of voluntary movements',
        'Brain Waves': ['Alpha waves', 'Beta waves'],
        'Frequency': '8-12 Hz (Alpha), 12-30 Hz (Beta)',
        'Data Processing (Short Term)': 'Moderate',
        'Data Processing (Long Term)': 'Moderate',
        'Neurons': 'Hundreds of millions',
        'Synapses': 'Billions'
    },
    'Discovery': {
        'Brain Parts': ['Frontal cortex', 'Parietal cortex', 'Temporal cortex'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Exploration and innovation',
        'Brain Waves': ['Theta waves'],
        'Frequency': '4-8 Hz',
        'Data Processing (Short Term)': 'High',
        'Data Processing (Long Term)': 'Moderate',
        'Neurons': 'Hundreds of millions',
        'Synapses': 'Billions'
    },
    'Memory': {
        'Brain Parts': ['Hippocampus', 'Amygdala', 'Prefrontal cortex'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Storage and retrieval of memories',
        'Brain Waves': ['Theta waves'],
        'Frequency': '3-8 Hz',
        'Data Processing (Short Term)': 'High',
        'Data Processing (Long Term)': 'High',
        'Neurons': 'Tens of millions',
        'Synapses': 'Hundreds of millions'
    },
    'Emotion': {
        'Brain Parts': ['Amygdala', 'Prefrontal cortex', 'Insular cortex'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Processing emotional responses and regulation',
        'Brain Waves': ['Theta waves'],
        'Frequency': '4-8 Hz',
        'Data Processing (Short Term)': 'Moderate',
        'Data Processing (Long Term)': 'Moderate',
        'Neurons': 'Tens of millions',
        'Synapses': 'Hundreds of millions'
    },
    'Decision Making': {
        'Brain Parts': ['Prefrontal cortex', 'Cingulate cortex', 'Basal ganglia'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Making complex decisions and planning',
        'Brain Waves': ['Theta waves', 'Beta waves'],
        'Frequency': '4-30 Hz',
        'Data Processing (Short Term)': 'Moderate',
        'Data Processing (Long Term)': 'High',
        'Neurons': 'Billions',
        'Synapses': 'Trillions'
    },
    'Attention': {
        'Brain Parts': ['Prefrontal cortex', 'Parietal cortex', 'Reticular activating system'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Focusing mental resources on stimuli or tasks',
        'Brain Waves': ['Beta waves', 'Gamma waves'],
        'Frequency': '12-100 Hz',
        'Data Processing (Short Term)': 'High',
        'Data Processing (Long Term)': 'Moderate',
        'Neurons': 'Billions',
        'Synapses': 'Trillions'
    },
    'Creativity': {
        'Brain Parts': ['Frontal cortex', 'Temporal cortex', 'Limbic system'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Generating new ideas and concepts',
        'Brain Waves': ['Alpha waves', 'Theta waves'],
        'Frequency': '8-12 Hz (Alpha), 4-8 Hz (Theta)',
        'Data Processing (Short Term)': 'Moderate',
        'Data Processing (Long Term)': 'Moderate',
        'Neurons': 'Billions',
        'Synapses': 'Trillions'
    },
    'Problem Solving': {
        'Brain Parts': ['Prefrontal cortex', 'Parietal cortex', 'Basal ganglia'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Finding solutions to complex problems',
        'Brain Waves': ['Beta waves', 'Gamma waves'],
        'Frequency': '12-100 Hz',
        'Data Processing (Short Term)': 'High',
        'Data Processing (Long Term)': 'High',
        'Neurons': 'Billions',
        'Synapses': 'Trillions'
    },
    'Learning': {
        'Brain Parts': ['Hippocampus', 'Cerebral cortex', 'Basal ganglia'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Acquiring new knowledge and skills',
        'Brain Waves': ['Theta waves', 'Gamma waves'],
        'Frequency': '4-8 Hz (Theta), 30-100 Hz (Gamma)',
        'Data Processing (Short Term)': 'High',
        'Data Processing (Long Term)': 'High',
        'Neurons': 'Billions',
        'Synapses': 'Trillions'
    },
    'Sleep': {
        'Brain Parts': ['Hypothalamus', 'Thalamus', 'Cerebral cortex'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Regulating sleep-wake cycles and brain maintenance',
        'Brain Waves': ['Delta waves', 'Theta waves'],
        'Frequency': '0.5-4 Hz (Delta), 4-8 Hz (Theta)',
        'Data Processing (Short Term)': 'Low',
        'Data Processing (Long Term)': 'Low',
        'Neurons': 'Hundreds of millions',
        'Synapses': 'Billions'
    },
    'Navigation': {
        'Brain Parts': ['Hippocampus', 'Entorhinal cortex', 'Parietal cortex'],
        'Locations': ['Both hemispheres'],
        'Functionality': 'Spatial orientation and memory for locations',
        'Brain Waves': ['Theta waves'],
        'Frequency': '4-8 Hz',
        'Data Processing (Short Term)': 'High',
        'Data Processing (Long Term)': 'Moderate',
        'Neurons': 'Tens of millions',
        'Synapses': 'Hundreds of millions'
    },
    'Social Interaction': {
    'Brain Parts': ['Prefrontal cortex', 'Temporal cortex', 'Mirror neurons'],
    'Locations': ['Both hemispheres'],
    'Functionality': 'Processing social cues, empathy, and interaction',
    'Brain Waves': ['Gamma waves'],
    'Frequency': '30-100 Hz',
    'Data Processing (Short Term)': 'High',
    'Data Processing (Long Term)': 'Moderate',
    'Neurons': 'Billions',
    'Synapses': 'Trillions'
},
'Music Processing': {
    'Brain Parts': ['Auditory cortex', 'Prefrontal cortex', 'Temporal lobe'],
    'Locations': ['Both hemispheres'],
    'Functionality': 'Processing musical stimuli and rhythm',
    'Brain Waves': ['Theta waves', 'Beta waves'],
    'Frequency': '4-8 Hz (Theta), 12-30 Hz (Beta)',
    'Data Processing (Short Term)': 'Moderate',
    'Data Processing (Long Term)': 'Moderate',
    'Neurons': 'Hundreds of millions',
    'Synapses': 'Billions'
},

'Executive Function': {
    'Brain Parts': ['Prefrontal cortex', 'Anterior cingulate cortex'],
    'Locations': ['Both hemispheres'],
    'Functionality': 'Planning, decision-making, and self-control',
    'Brain Waves': ['Beta waves', 'Gamma waves'],
    'Frequency': '12-30 Hz (Beta), 30-100 Hz (Gamma)',
    'Data Processing (Short Term)': 'High',
    'Data Processing (Long Term)': 'High',
    'Neurons': 'Billions',
    'Synapses': 'Trillions'
},

'Reward and Motivation': {
    'Brain Parts': ['Nucleus accumbens', 'Ventral tegmental area', 'Prefrontal cortex'],
    'Locations': ['Both hemispheres'],
    'Functionality': 'Processing rewards, pleasure, and motivation',
    'Brain Waves': ['Gamma waves'],
    'Frequency': '30-100 Hz',
    'Data Processing (Short Term)': 'High',
    'Data Processing (Long Term)': 'Moderate',
    'Neurons': 'Hundreds of millions',
    'Synapses': 'Billions'
},

'Self-Awareness': {
    'Brain Parts': ['Prefrontal cortex', 'Insular cortex'],
    'Locations': ['Both hemispheres'],
    'Functionality': 'Consciousness, introspection, and self-perception',
    'Brain Waves': ['Alpha waves', 'Theta waves'],
    'Frequency': '8-12 Hz (Alpha), 4-8 Hz (Theta)',
    'Data Processing (Short Term)': 'Moderate',
    'Data Processing (Long Term)': 'Moderate',
    'Neurons': 'Billions',
    'Synapses': 'Trillions'
}

}

# Preparing data for the table
table_data = []

for function, details in functions.items():
    row = [function, ', '.join(details['Brain Parts']), ', '.join(details['Locations']), details['Functionality'],
           ', '.join(details['Brain Waves']), details['Frequency'], details['Data Processing (Short Term)'],
           details['Data Processing (Long Term)'], details['Neurons'], details['Synapses']]
    table_data.append(row)

# Define the table header
headers = ["Brain Function", "Brain Parts", "Locations", "Functionality", "Brain Waves", "Frequency",
           "Data Processing (Short Term)", "Data Processing (Long Term)", "Neurons", "Synapses"]

# Generate the table string with tabulate
table_str = tabulate(table_data, headers, tablefmt="grid")

# Set up the plot
fig, ax = plt.subplots(figsize=(20, 15))
ax.axis('off')
ax.axis('tight')

# Create the table and set row and column heights
table = ax.table(cellText=table_data, colLabels=headers, cellLoc='center', loc='center')

# Adjust column widths and row heights
table.auto_set_column_width([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
table.auto_set_font_size(False)
table.set_fontsize(10)

# Adjust row heights to fit text
for key, cell in table.get_celld().items():
    cell.set_height(cell.get_height() * 2.5)  # Increase row height

# Save the table as an image
plt.savefig("enhanced_brain_functions_table_wide.png", bbox_inches='tight', dpi=300)

# Display the table
img = Image.open("enhanced_brain_functions_table_wide.png")
img.show()
