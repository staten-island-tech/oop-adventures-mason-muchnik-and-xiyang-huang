

## **Q1. Building a Class with a Decision Method**

Write Python code to complete the following tasks.

### **a)** Create a class called `ThemeParkPass`.

The class should include the following properties.
Next to each property, clearly identify the **data type**:

* `guest_name`
* `pass_type` (examples: `"Basic"`, `"Premium"`)
* `rides_used` (a list of ride names)
* `ride_limit`
* `is_valid`

---

### **b)** Add a method called `can_ride(ride_name)` that:

* Returns `False` if the pass is **not valid**
* Returns `False` if the number of rides used is **already at the ride limit**
* Otherwise:

  * Add the `ride_name` to `rides_used`
  * Return `True`

*(This method should both **make a decision** and **update the object** when allowed.)*

---

### **c)** Create **one instance** of the `ThemeParkPass` class for a fictional guest.

---

## **Q2. Functions & Lists of Objects**

You are given a list of `ThemeParkPass` objects created from the class above.

Write a function called `count_premium_passes` that:

* Accepts **one parameter**:

  * a list of `ThemeParkPass` objects
* Returns the **number of passes** where `pass_type` is `"Premium"` **and** `is_valid` is `True`

