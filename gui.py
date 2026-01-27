import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import math


class BisectionMethodGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bisection Method Solver - Enhanced Precision")
        self.root.geometry("1000x750")

        # Set style
        self.root.configure(bg='#f0f0f0')

        # Title
        title_label = tk.Label(root, text="Bisection Method Calculator - Enhanced Precision",
                               font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=15)

        # Main frame
        main_frame = tk.Frame(root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=30, pady=10)

        # Input Frame
        input_frame = tk.LabelFrame(main_frame, text="Input Parameters",
                                    font=('Arial', 12, 'bold'), bg='#f0f0f0',
                                    fg='#34495e', padx=20, pady=15)
        input_frame.pack(fill='x', pady=(0, 15))

        # Function input
        tk.Label(input_frame, text="f(x) =", font=('Arial', 11),
                 bg='#f0f0f0').grid(row=0, column=0, padx=(0, 10), pady=10, sticky='w')

        self.function_entry = tk.Entry(input_frame, font=('Arial', 11), width=50)
        self.function_entry.grid(row=0, column=1, columnspan=4, padx=(0, 10), pady=10, sticky='w')
        self.function_entry.insert(0, "math.sin(x) - x/2")

        # Examples label
        examples = [
            "Examples:",
            "math.sin(x) - x/2",
            "x**3 - 2*x - 5",
            "math.exp(-x) - x",
            "math.cos(x) - x"
        ]

        for i, example in enumerate(examples):
            tk.Label(input_frame, text=example,
                     font=('Arial', 9), bg='#f0f0f0', fg='#7f8c8d').grid(
                row=1 + i, column=1, columnspan=4, pady=(0, 5), sticky='w')

        # Interval inputs
        tk.Label(input_frame, text="Interval [a, b]:", font=('Arial', 11),
                 bg='#f0f0f0').grid(row=5, column=0, padx=(0, 10), pady=10, sticky='w')

        tk.Label(input_frame, text="a =", font=('Arial', 11),
                 bg='#f0f0f0').grid(row=5, column=1, padx=(0, 5), pady=10, sticky='w')
        self.a_entry = tk.Entry(input_frame, font=('Arial', 11), width=15)
        self.a_entry.grid(row=5, column=2, padx=(0, 20), pady=10, sticky='w')
        self.a_entry.insert(0, "1.0")

        tk.Label(input_frame, text="b =", font=('Arial', 11),
                 bg='#f0f0f0').grid(row=5, column=3, padx=(0, 5), pady=10, sticky='w')
        self.b_entry = tk.Entry(input_frame, font=('Arial', 11), width=15)
        self.b_entry.grid(row=5, column=4, padx=(0, 10), pady=10, sticky='w')
        self.b_entry.insert(0, "2.0")

        # Tolerance input with dropdown
        tk.Label(input_frame, text="Precision Settings:", font=('Arial', 11),
                 bg='#f0f0f0').grid(row=6, column=0, padx=(0, 10), pady=10, sticky='w')

        # Tolerance type
        self.tolerance_type = tk.StringVar(value="absolute")
        tk.Radiobutton(input_frame, text="Absolute Error", variable=self.tolerance_type,
                       value="absolute", bg='#f0f0f0').grid(row=6, column=1, sticky='w')
        tk.Radiobutton(input_frame, text="Relative Error", variable=self.tolerance_type,
                       value="relative", bg='#f0f0f0').grid(row=6, column=2, sticky='w')

        # Tolerance value
        tk.Label(input_frame, text="Tolerance (ε):", font=('Arial', 11),
                 bg='#f0f0f0').grid(row=7, column=0, padx=(0, 10), pady=10, sticky='w')

        self.tolerance_entry = tk.Entry(input_frame, font=('Arial', 11), width=15)
        self.tolerance_entry.grid(row=7, column=1, padx=(0, 10), pady=10, sticky='w')
        self.tolerance_entry.insert(0, "1e-8")

        # Max iterations
        tk.Label(input_frame, text="Max Iterations:", font=('Arial', 11),
                 bg='#f0f0f0').grid(row=7, column=2, padx=(20, 5), pady=10, sticky='w')

        self.max_iter_entry = tk.Entry(input_frame, font=('Arial', 11), width=10)
        self.max_iter_entry.grid(row=7, column=3, padx=(0, 10), pady=10, sticky='w')
        self.max_iter_entry.insert(0, "100")

        # Button Frame
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill='x', pady=(0, 15))

        buttons = [
            ("Calculate Root", '#3498db', self.calculate_root),
            ("Clear Results", '#e74c3c', self.clear_results),
            ("Plot Function", '#2ecc71', self.plot_function),
            ("Export Results", '#9b59b6', self.export_results)
        ]

        for text, color, command in buttons:
            btn = tk.Button(button_frame, text=text,
                            font=('Arial', 11, 'bold'), bg=color,
                            fg='white', padx=15, pady=6,
                            command=command)
            btn.pack(side='left', padx=(0, 15))

        # Results Frame
        results_frame = tk.LabelFrame(main_frame, text="Results",
                                      font=('Arial', 12, 'bold'), bg='#f0f0f0',
                                      fg='#34495e', padx=20, pady=15)
        results_frame.pack(fill='both', expand=True)

        # Statistics frame
        stats_frame = tk.Frame(results_frame, bg='#f0f0f0')
        stats_frame.pack(fill='x', pady=(0, 15))

        stats = [
            ("root_label", "Root: ", 0),
            ("iter_label", "Iterations: ", 1),
            ("error_label", "Absolute Error: ", 2),
            ("interval_label", "Final Interval: ", 3),
            ("fvalue_label", "f(root) = ", 4)
        ]

        for var_name, text, col in stats:
            label = tk.Label(stats_frame, text=text, font=('Arial', 11),
                             bg='#f0f0f0', fg='#2c3e50')
            label.grid(row=0, column=col * 2, padx=(0, 5), pady=5, sticky='w')

            value_label = tk.Label(stats_frame, text="", font=('Arial', 11, 'bold'),
                                   bg='#f0f0f0', fg='#e74c3c')
            value_label.grid(row=0, column=col * 2 + 1, padx=(0, 20), pady=5, sticky='w')
            setattr(self, var_name, value_label)

        # Results table with scrollbar
        table_frame = tk.Frame(results_frame)
        table_frame.pack(fill='both', expand=True)

        # Create Treeview with more columns
        columns = ('Iter', 'a', 'b', 'c', 'f(c)', 'Error', 'Interval Size')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=12)

        # Define columns
        column_widths = {
            'Iter': 70, 'a': 100, 'b': 100, 'c': 120,
            'f(c)': 120, 'Error': 100, 'Interval Size': 100
        }

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths.get(col, 100), anchor='center')

        # Add scrollbars
        v_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(table_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        # Pack
        self.tree.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew', columnspan=2)
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # Console output
        console_frame = tk.LabelFrame(main_frame, text="Detailed Output",
                                      font=('Arial', 12, 'bold'), bg='#f0f0f0',
                                      fg='#34495e', padx=20, pady=15)
        console_frame.pack(fill='both', expand=True, pady=(15, 0))

        self.console_text = scrolledtext.ScrolledText(console_frame, height=10,
                                                      font=('Consolas', 10), wrap=tk.WORD)
        self.console_text.pack(fill='both', expand=True)

        # Status bar
        self.status_bar = tk.Label(root, text="Ready - Enter function and interval",
                                   bd=1, relief=tk.SUNKEN, anchor=tk.W,
                                   bg='#ecf0f1', fg='#2c3e50', font=('Arial', 10))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def evaluate_function(self, func_str, x):
        """Safely evaluate the function at point x with high precision"""
        try:
            namespace = {'math': math, 'x': float(x)}
            return float(eval(func_str, {"__builtins__": {}}, namespace))
        except Exception as e:
            raise ValueError(f"Error evaluating function at x={x}: {e}")

    def calculate_root(self):
        """Perform bisection method calculation with enhanced precision"""
        # Clear previous results
        self.clear_table()
        self.console_text.delete(1.0, tk.END)

        try:
            # Get inputs
            func_str = self.function_entry.get()
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            epsilon = float(self.tolerance_entry.get())
            max_iter = int(self.max_iter_entry.get())
            tol_type = self.tolerance_type.get()

            # Validate inputs
            if a >= b:
                messagebox.showerror("Input Error", "a must be less than b")
                return

            if epsilon <= 0:
                messagebox.showerror("Input Error", "Tolerance must be positive")
                return

            # Update status
            self.status_bar.config(text="Calculating with enhanced precision...")
            self.root.update()

            # Evaluate f(a) and f(b)
            fa = self.evaluate_function(func_str, a)
            fb = self.evaluate_function(func_str, b)

            # Check initial condition
            if fa == 0:
                self.display_results(0, a, fa, a, b, 0, 0)
                return
            if fb == 0:
                self.display_results(0, b, fb, a, b, 0, 0)
                return

            if fa * fb > 0:
                messagebox.showerror("Error",
                                     f"No root guaranteed in interval [{a}, {b}]\n"
                                     f"f({a}) = {fa:.12f}\n"
                                     f"f({b}) = {fb:.12f}\n"
                                     f"f(a) * f(b) = {fa * fb:.12f} > 0")
                return

            iteration = 0
            c_prev = a  # For relative error calculation
            interval_size = abs(b - a)

            # Console output header
            self.console_text.insert(tk.END,
                                     f"{'=' * 60}\n")
            self.console_text.insert(tk.END,
                                     f"BISECTION METHOD - ENHANCED PRECISION\n")
            self.console_text.insert(tk.END,
                                     f"{'=' * 60}\n")
            self.console_text.insert(tk.END,
                                     f"Function: f(x) = {func_str}\n")
            self.console_text.insert(tk.END,
                                     f"Interval: [{a:.12f}, {b:.12f}]\n")
            self.console_text.insert(tk.END,
                                     f"Tolerance: {epsilon} ({tol_type} error)\n")
            self.console_text.insert(tk.END,
                                     f"Max iterations: {max_iter}\n")
            self.console_text.insert(tk.END,
                                     f"{'-' * 60}\n")

            # Perform bisection iterations with enhanced stopping criteria
            while iteration < max_iter:
                iteration += 1

                # Compute midpoint with high precision
                c = (a + b) / 2.0
                fc = self.evaluate_function(func_str, c)

                # Calculate errors
                interval_size = abs(b - a)
                abs_error = abs(fc)

                # Calculate relative error if not first iteration
                if iteration > 1:
                    rel_error = abs(c - c_prev) / abs(c) if c != 0 else float('inf')
                else:
                    rel_error = float('inf')

                # Add to table with more precision
                self.tree.insert('', 'end', values=(
                    iteration,
                    f"{a:.12f}",
                    f"{b:.12f}",
                    f"{c:.12f}",
                    f"{fc:.2e}",
                    f"{abs_error:.2e}",
                    f"{interval_size:.2e}"
                ))

                # Enhanced stopping criteria
                stop = False
                stop_reason = ""

                if tol_type == "absolute":
                    if abs_error < epsilon:
                        stop = True
                        stop_reason = f"|f(c)| < {epsilon}"
                    elif interval_size < epsilon:
                        stop = True
                        stop_reason = f"Interval size < {epsilon}"
                else:  # relative error
                    if rel_error < epsilon and iteration > 1:
                        stop = True
                        stop_reason = f"Relative error < {epsilon}"

                # Check if exact root found
                if fc == 0:
                    stop = True
                    stop_reason = "Exact root found (f(c) = 0)"

                if stop:
                    self.console_text.insert(tk.END,
                                             f"\nStopping criterion met: {stop_reason}\n")
                    break

                # Update interval
                if fa * fc < 0:
                    b = c
                    fb = fc
                else:
                    a = c
                    fa = fc

                c_prev = c

            else:
                self.console_text.insert(tk.END,
                                         f"\nWarning: Maximum iterations ({max_iter}) reached\n")

            # Display final results
            self.display_results(iteration, c, fc, a, b, abs_error, interval_size)

            # Final console output
            self.console_text.insert(tk.END,
                                     f"{'=' * 60}\n")
            self.console_text.insert(tk.END,
                                     f"FINAL RESULTS:\n")
            self.console_text.insert(tk.END,
                                     f"Approximate root: {c:.15f}\n")
            self.console_text.insert(tk.END,
                                     f"f(root) = {fc:.2e}\n")
            self.console_text.insert(tk.END,
                                     f"Absolute error: {abs_error:.2e}\n")
            self.console_text.insert(tk.END,
                                     f"Final interval: [{a:.12f}, {b:.12f}]\n")
            self.console_text.insert(tk.END,
                                     f"Interval size: {interval_size:.2e}\n")
            self.console_text.insert(tk.END,
                                     f"Iterations: {iteration}\n")

            self.status_bar.config(text=f"Calculation completed - Root: {c:.10f}")

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            self.status_bar.config(text="Error: Invalid input")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.status_bar.config(text="Error during calculation")

    def display_results(self, iteration, c, fc, a, b, abs_error, interval_size):
        """Display results in the GUI"""
        self.root_label.config(text=f"{c:.15f}")
        self.iter_label.config(text=str(iteration))
        self.error_label.config(text=f"{abs_error:.2e}")
        self.interval_label.config(text=f"[{a:.6f}, {b:.6f}]")
        self.fvalue_label.config(text=f"{fc:.2e}")

    def clear_table(self):
        """Clear all items from the treeview"""
        for item in self.tree.get_children():
            self.tree.delete(item)

    def clear_results(self):
        """Clear all results and console"""
        self.clear_table()
        self.console_text.delete(1.0, tk.END)
        self.root_label.config(text="")
        self.iter_label.config(text="")
        self.error_label.config(text="")
        self.interval_label.config(text="")
        self.fvalue_label.config(text="")
        self.status_bar.config(text="Results cleared - Ready for new calculation")

    def plot_function(self):
        """Plot the function with root visualization"""
        try:
            import matplotlib.pyplot as plt
            import numpy as np

            func_str = self.function_entry.get()
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())

            # Extended range for better visualization
            margin = (b - a) * 0.5
            x_min = a - margin
            x_max = b + margin

            # Generate x values
            x_vals = np.linspace(x_min, x_max, 1000)
            y_vals = [self.evaluate_function(func_str, x) for x in x_vals]

            # Create figure with subplots
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), height_ratios=[2, 1])

            # Main plot
            ax1.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'$f(x) = {func_str}$')
            ax1.axhline(y=0, color='k', linestyle='-', alpha=0.3)
            ax1.axvline(x=a, color='g', linestyle='--', alpha=0.7, label=f'$a = {a:.4f}$')
            ax1.axvline(x=b, color='r', linestyle='--', alpha=0.7, label=f'$b = {b:.4f}$')

            # Shade the interval
            ax1.axvspan(a, b, alpha=0.1, color='yellow')

            # Plot root if calculated
            if self.root_label.cget("text"):
                root_x = float(self.root_label.cget("text"))
                root_y = self.evaluate_function(func_str, root_x)
                ax1.plot(root_x, root_y, 'ro', markersize=10,
                         label=f'Root $\\approx {root_x:.8f}$')
                ax1.plot([root_x, root_x], [0, root_y], 'r--', alpha=0.5)

            ax1.set_xlabel('$x$', fontsize=12)
            ax1.set_ylabel('$f(x)$', fontsize=12)
            ax1.set_title('Bisection Method - Function Visualization', fontsize=14, fontweight='bold')
            ax1.grid(True, alpha=0.3)
            ax1.legend(loc='best')

            # Zoomed plot around root
            if self.root_label.cget("text"):
                root_x = float(self.root_label.cget("text"))
                zoom = margin * 0.1
                x_zoom = np.linspace(root_x - zoom, root_x + zoom, 500)
                y_zoom = [self.evaluate_function(func_str, x) for x in x_zoom]

                ax2.plot(x_zoom, y_zoom, 'b-', linewidth=2)
                ax2.axhline(y=0, color='k', linestyle='-', alpha=0.3)
                ax2.plot(root_x, root_y, 'ro', markersize=8)
                ax2.plot([root_x, root_x], [0, root_y], 'r--', alpha=0.5)

                # Add tolerance band
                if self.tolerance_entry.get():
                    epsilon = float(self.tolerance_entry.get())
                    ax2.axhspan(-epsilon, epsilon, alpha=0.1, color='green',
                                label=f'Tolerance band: $\\pm{epsilon}$')

                ax2.set_xlabel('$x$ (zoomed)', fontsize=12)
                ax2.set_ylabel('$f(x)$', fontsize=12)
                ax2.set_title(f'Zoomed View Around Root (x ≈ {root_x:.8f})', fontsize=12)
                ax2.grid(True, alpha=0.3)
                ax2.legend(loc='best')

            plt.tight_layout()
            plt.show()
            self.status_bar.config(text="Plot displayed successfully")

        except ImportError:
            messagebox.showerror("Error",
                                 "Matplotlib is not installed.\n"
                                 "Install it using: pip install matplotlib")
        except Exception as e:
            messagebox.showerror("Error", f"Cannot plot function: {e}")

    def export_results(self):
        """Export results to a text file"""
        try:
            from tkinter import filedialog
            import os

            # Ask for save location
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                initialfile="bisection_results.txt"
            )

            if not filename:
                return

            # Collect data
            lines = []
            lines.append("=" * 60)
            lines.append("BISECTION METHOD RESULTS")
            lines.append("=" * 60)
            lines.append(f"Function: f(x) = {self.function_entry.get()}")
            lines.append(f"Interval: [{self.a_entry.get()}, {self.b_entry.get()}]")
            lines.append(f"Tolerance: {self.tolerance_entry.get()}")
            lines.append(f"Tolerance type: {self.tolerance_type.get()}")
            lines.append("")

            # Add results
            if self.root_label.cget("text"):
                lines.append("FINAL RESULTS:")
                lines.append(f"Approximate root: {self.root_label.cget('text')}")
                lines.append(f"Iterations: {self.iter_label.cget('text')}")
                lines.append(f"Absolute error: {self.error_label.cget('text')}")
                lines.append(f"Final interval: {self.interval_label.cget('text')}")
                lines.append(f"f(root): {self.fvalue_label.cget('text')}")
                lines.append("")

            # Add iteration table
            lines.append("ITERATION HISTORY:")
            lines.append("-" * 100)

            # Get column headers
            headers = []
            for col in self.tree['columns']:
                headers.append(self.tree.heading(col)['text'])
            lines.append("\t".join(headers))
            lines.append("-" * 100)

            # Get data rows
            for item in self.tree.get_children():
                values = self.tree.item(item)['values']
                lines.append("\t".join(map(str, values)))

            # Write to file
            with open(filename, 'w') as f:
                f.write("\n".join(lines))

            messagebox.showinfo("Export Successful",
                                f"Results exported to:\n{os.path.basename(filename)}")
            self.status_bar.config(text=f"Results exported to {os.path.basename(filename)}")

        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export results: {e}")


def main():
    root = tk.Tk()
    app = BisectionMethodGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()