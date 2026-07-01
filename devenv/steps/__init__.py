import importlib
import pkgutil


def discover() -> list:
    steps = []
    package = importlib.import_module(__name__)
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        if module_name.startswith("_") or module_name == "base":
            continue
        module = importlib.import_module(f"{__name__}.{module_name}")
        if hasattr(module, "STEP"):
            steps.append(module.STEP)
        if hasattr(module, "STEPS"):
            steps.extend(module.STEPS)
    return steps
