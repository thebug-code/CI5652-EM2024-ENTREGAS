CXX := g++
CXXFLAGS := -std=c++11 -Wall
SRCS := contar_subarreglos_buenos.cpp
OBJS := $(SRCS:.cpp=.o)
EXECUTABLE := runContarSubArreglosBuenos

$(EXECUTABLE): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $<

clean:
	rm -f $(OBJS) $(EXECUTABLE)
