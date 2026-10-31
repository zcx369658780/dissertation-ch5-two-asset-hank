# Source pair and scope

MATLAB fixed science ref56447829ce0e6c3c85552c53c351b26a2452a4bd, path validators/multi_province/call725_policy_operator_stability/matlab_trajectory.m, Blob0e38270154ab8953290ae3ef6c92f95d38230afb. Only lines110-130 axis_operator are embedded exactly in the new short runner. The full historical trajectory contains HJB/solve code and is never executed. Python Blob9a511e151c9bf449412dc5605dfa1a2076711277 and indexing Blob3aee864af5dce5128957896e5d7803c2a815aab6 were compiled from exact authenticated current snapshots as genuine modules.

MATLAB axis1 maps to Python axis0, neighbors +/-1; MATLAB axis2 maps to Python axis1, neighbors +/-I. Row1=i1+(j1-1)*I+(z1-1)*I*J; k0=i0+I*(j0+J*z0). Both skip outward neighbors while retaining -(rb+rf) diagonal. Source kron(switch,eye(I*J)) and A=BB+AAH+Bswitch are matched. No row-conservation repair, clipping or economic drift recalculation.

The indexing docstring uses generic(a,b,z) names and exposes a separate matlab_to_canonical transpose. That transpose is not called: this contract uses identical logical(I,J,Nz) input and direct axis pairing. This does not prove global economic b/a policy mapping. The MATLAB anchor is historical source-extracted code, not original main2.m. Positive and mutated-source negative gates passed; actual Python assembly ran. Host blocked MATLAB, so all cross-language numeric parity is NOT_TESTED.

Exact extracted function:

    function G=axis_operator(backward,forward,axis_number)
    shape=size(backward); I=shape(1); J=shape(2); Nz=shape(3); M=I*J*Nz;
    rows=[]; cols=[]; vals=[];
    for nz=1:Nz
     for j=1:J
      for i=1:I
       row=i+(j-1)*I+(nz-1)*I*J; rb=backward(i,j,nz); rf=forward(i,j,nz); total=rb+rf;
       if rb~=0
        if (axis_number==1 && i>1); col=row-1; elseif (axis_number==2 && j>1); col=row-I; else; col=0; end
        if col>0; rows(end+1)=row; cols(end+1)=col; vals(end+1)=rb; end
       end
       if rf~=0
        if (axis_number==1 && i<I); col=row+1; elseif (axis_number==2 && j<J); col=row+I; else; col=0; end
        if col>0; rows(end+1)=row; cols(end+1)=col; vals(end+1)=rf; end
       end
       rows(end+1)=row; cols(end+1)=row; vals(end+1)=-total;
      end
     end
    end
    G=sparse(rows,cols,vals,M,M);
    end
