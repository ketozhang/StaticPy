---
title: Young's Double Slit for Electrons
---

Using the famous Young's double slit experiment we can see one of the most interesting properties of quantum particles; for now, let's focus on the electron.

The experiment is set up like any Young's double slit but this time we will use an electron gun (like a cathode ray tube). There's two version of this gun quoted in literature, one that shoots lumps or electron or one that shoots a single electron at a time. I prefer a single electron for simplicity.

## Experiment 1 - Unobserved

The first experiment is set up doing 3 tasks with 3 probabilities:

* $P_1$ for the probability if we only allow the electron to go through slit 1 by closing slit 2.
* $P_2$ for the probability if we only allow the electron to go through slit 2 by closing slit 1.
* $P_{12}$ for the probability if we allow both slits to be open

The result show that the electron follows the property of waves:

* The probability distribution of $P_{12}$ is not particle-like such that it's the sum of $P_1 + P_2$,

    $$ P_{12} \neq P_1 + P_2$$
    
    Instead the electron is actually wave-like such that we define $P_1 = \lvert \phi_1 \rvert^2$ and $P_2 = \lvert \phi_2 \rvert^2$,

    $$
    \begin{equation}
        P_{12} =  \lvert \phi_1 + \phi_2 \rvert^2
        %\label{eq:slit probability}
    \end{equation}
    $$

* Each electron does not necessrily only have to pass through one slit. It may be pass through multiple or something else. No answer have been agreed upon.

## Experiment 2 - Observed

In this experiment instead of covering the hole, we place a detector at each hole to determine if the electron that landed at the wall comes from slit 1 or slit 2. 

The results show that the electron follows the property of particles:

* The probability distribution $P_{12}$ is as we expected:

$$ P_{12} = P_1 + P_2 $$

* It is necessary that the electron either pass on to slit 1 or slit 2.
* The difference between this experiement is that the electron interacts with the detector (which emits photons)

## Conclusion
We have two experiment one shows that the electron is wave-like if we were not to disturb the electron as it travels to the wall and an electron that is particle-like if we do.

One may wonder if we vary the detector's emission so that it distrubs the electrons less we find that:

* Decreasing the intensity of the detector only shows the probability that an electron is either wave-like (photon does not hit the electron) or particle-like (photon does hit the electron). This result is trivial to us.
* Decreasing the wavelength of the detector is much more interesting. We see that at a certain lower limit wavelength it is **impossible** to tell whether an electron came from slit 1 or slit 2. If the wavelength is much greater than the distance between slit 1 and slit 2 detectors then we will not be able to tell which detector it comes from (Rayleigh criterion). We consider this experiment inconclusive because it's an experimental limit we cannot observe.

The experimental limit above is one of the fundamental properties of not only quantum mechanics but of the universe. This limit is most famously called the **Heisenberg uncertainty principle**.
