// Elementos del DOM
const form = document.getElementById("multiStepForm"); // Formulario completo
const steps = form.querySelectorAll(".form-step"); // Todos los pasos
const progressBar = form.querySelector(".progress-bar"); // Barra de progreso
const progressText = form.querySelector(".progress-text"); // Texto "Step X of Y"
const totalSteps = steps.length; // Total de pasos (3)

let currentStep = 0; // Paso actual (empieza en 0)

// Actualiza la barra de progreso y el texto
function updateProgress() {
  const percent = ((currentStep + 1) / totalSteps) * 100; // Calcula el porcentaje
  progressBar.style.width = percent + "%"; // Ancha la barra
  progressText.textContent = `Step ${currentStep + 1} of ${totalSteps}`; // Actualiza texto
}

// Muestra un paso específico y oculta los demás
function showStep(index) {
  steps.forEach((step, i) => {
    // toggle: agrega "active" solo al paso actual, quita a los demás
    step.classList.toggle("active", i === index);
  });
  updateProgress(); // Actualiza la barra
}

// Botones "Next": avanzan al siguiente paso
form.querySelectorAll(".next-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    if (currentStep < totalSteps - 1) { // Si no es el último paso
      currentStep++; // Avanza
      showStep(currentStep); // Muestra el nuevo paso
    }
  });
});

// Botones "Previous": retroceden al paso anterior
form.querySelectorAll(".prev-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    if (currentStep > 0) { // Si no es el primer paso
      currentStep--; // Retrocede
      showStep(currentStep); // Muestra el paso anterior
    }
  });
});

// Muestra el primer paso al cargar la página
showStep(currentStep);

// Envío del formulario
form.addEventListener("submit", (e) => {
  e.preventDefault(); // Evita que la página se recargue
  alert("Form submitted!"); // Muestra mensaje de éxito
});
