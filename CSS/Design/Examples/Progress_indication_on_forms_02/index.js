// Elementos del DOM
const form = document.getElementById("progressForm"); // Formulario completo
const steps = form.querySelectorAll(".form-step"); // Todos los pasos
const progressBar = form.querySelector(".progress-bar"); // Barra de progreso
const currentStepSpan = document.getElementById("currentStep"); // Span del paso actual
const totalStepsSpan = document.getElementById("totalSteps"); // Span del total de pasos
const percentageSpan = document.getElementById("percentage"); // Span del porcentaje

const totalSteps = steps.length; // Total de pasos (4)
let currentStep = 0; // Paso actual (empieza en 0)

// Inicializa el total de pasos en el HTML
totalStepsSpan.textContent = totalSteps;

// Actualiza la barra de progreso, los spans y los atributos ARIA
function updateProgress() {
  const percent = Math.round(((currentStep + 1) / totalSteps) * 100); // Porcentaje redondeado
  progressBar.style.width = percent + "%"; // Ancha la barra
  currentStepSpan.textContent = currentStep + 1; // Actualiza "Step X"
  percentageSpan.textContent = percent + "%"; // Actualiza "Z%"

  // Actualiza atributo ARIA para accesibilidad
  form
    .querySelector(".progress-container")
    .setAttribute("aria-valuenow", percent);
}

// Muestra un paso específico y oculta los demás
function showStep(index) {
  steps.forEach((step, i) => {
    // toggle: agrega "active" solo al paso actual
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

// Envío del formulario
form.addEventListener("submit", (e) => {
  e.preventDefault(); // Evita que la página se recargue
  alert("Form submitted! Thanks!"); // Muestra mensaje de éxito
});

// Muestra el primer paso al cargar la página
showStep(currentStep);
